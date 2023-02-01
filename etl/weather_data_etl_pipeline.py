#!/usr/bin/env python3

import pandas as pd
import requests
import json
from constants import api_url, table_name
from utils import get_postgres_connection, close_postgres_connection


def get_api_response(api_url):
    # Get API response and convert to JSON Object
    response = requests.get(api_url)
    json_response = None

    if response.status_code == 200:
        try:
            json_response = response.json()
            print(json_response)
        except json.decoder.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
    else:
        print(f"Request failed with status code: {response.status_code}")

    return json_response


def transform_weather_data(json_response):
    # Get the list of days from the JSON object
    days_list = json_response["days"]

    # Extract hours from the list
    hours_list = []
    for d in days_list:
        for hour in d["hours"]:
            hours_list.append({
                "datetime": hour["datetime"],
                "humidity": hour["humidity"],
                "temp": hour["temp"]
            })

    # Create pandas dataframe
    df = pd.DataFrame(hours_list, columns=["datetime", "humidity", "temp"])
    df["date"] = pd.to_datetime(df["datetime"]).dt.date

    return df


def load_weather_data(df, conn, cursor, table_name):
    # Create table with the name referring to the dbname variable
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS {} (
            id SERIAL PRIMARY KEY,
            date DATE,
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
            """.format(table_name), (row['date'], row['humidity']))
    conn.commit()


def view_weather_table_data(cursor, table_name):
    # Select and print the data from the table
    cursor.execute("""
        SELECT * FROM {};
        """.format(table_name))

    rows = cursor.fetchall()
    for row in rows:
        print(row)


api_response = get_api_response(api_url)
df = transform_weather_data(api_response)
conn, cursor = get_postgres_connection()
load_weather_data(df, conn, cursor, table_name)
view_weather_table_data(cursor, table_name)
close_postgres_connection(conn, cursor)
