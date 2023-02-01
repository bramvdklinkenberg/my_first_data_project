#!/usr/bin/env python3

from constants import (
    storage_container_name,
    csv_filename,
    account_url,
    host,
    user,
    password,
    dbname,
    sslmode
    )
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobClient
import psycopg2


def get_blob_client():
    # BlobClient using DefaultAzureCredential for authentication
    credential = DefaultAzureCredential()
    blob_client = BlobClient(
        account_url,
        container_name=storage_container_name,
        blob_name=csv_filename,
        credential=credential
        )

    return blob_client


def get_postgres_connection():
    # Connect to Azure PostgreSQL using psycopg2
    conn = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        dbname=dbname,
        sslmode=sslmode
    )
    cursor = conn.cursor()

    return conn, cursor


def close_postgres_connection(conn, cursor):
    # Close the connection to Azure PostgreSQL
    cursor.close()
    conn.close()
