#!/usr/bin/env python3

import pandas as pd
from utils import (
    get_blob_client,
    get_postgres_connection,
    close_postgres_connection
    )
from constants import table_name


def extract_csv_data(blob_client):
    # Download the contents of the csv file
    csv_content = blob_client.download_blob()

    return csv_content


def convert_csv_to_dataframe(csv_content):
    # Convert csv to pandas dataframe
    df = pd.read_csv(csv_content)

    return df


def transform_humidity_data(df):
    # Delete the columns Remark and Unnamed
    df = df.drop(columns=['Remark', 'Unnamed: 4'])

    # Set all column names to lowercase
    df.columns = map(str.lower, df.columns)

    # Rename the Vochtigheid column to Humidity
    df.rename(columns={'vochtigheid': 'humidity'}, inplace=True)

    # Remove Celsius symbol from the Temp column
    df['temp'] = df['temp'].str.replace('℃', '')
    # Remove Percentage symbol from the Vochtigheid column
    df['humidity'] = df['humidity'].str.replace('%', '')

    # Set the correct column types
    df = df.astype({'temp': 'float', 'humidity': 'float'})
    df['date'] = df['date'].astype('datetime64[ns]')

    return df


def load_humidity_data(df, conn, cursor, table_name):
    # Create table with the name referring to the dbname variable
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS {} (
            id SERIAL PRIMARY KEY,
            date TIMESTAMP,
            temp FLOAT,
            humidity FLOAT
        );
        """.format(table_name))
    conn.commit()

    # Insert the data into the table
    for index, row in df.iterrows():
        cursor.execute("""
            INSERT INTO {} (date, temp, humidity)
            VALUES (%s, %s, %s);
            """.format(table_name), (row['date'], row['temp'], row['humidity']))
    conn.commit()


def view_table_name_data(cursor, table_name):
    # Select and print the data from the table
    cursor.execute("""
        SELECT * FROM {};
        """.format(table_name))

    rows = cursor.fetchall()
    for row in rows:
        print(row)


blob_client = get_blob_client()
csv_content = extract_csv_data(blob_client)
df = convert_csv_to_dataframe(csv_content)
df = transform_humidity_data(df)
conn, cursor = get_postgres_connection()
load_humidity_data(df, conn, cursor, table_name)
view_table_name_data(cursor, table_name)
close_postgres_connection(conn, cursor)
