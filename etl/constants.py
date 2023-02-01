#!/usr/bin/env python3

import os

# Storage account variables
storage_account_name = os.environ["AZURE_STORAGE_ACCOUNT_NAME"]
account_url = "https://" + storage_account_name + ".blob.core.windows.net"
storage_container_name = os.environ["AZURE_STORAGE_CONTAINER_NAME"]
csv_filename = os.environ["CSV_FILENAME"]

# PostgreSQL variables
host = os.environ["AZURE_POSTGRESQL_HOSTNAME"]
user = os.environ["AZURE_POSTGRESQL_ADMIN"]
password = os.environ["AZURE_POSTGRESQL_ADMIN_PASSWORD"]
dbname = os.environ["AZURE_POSTGRESQL_DBNAME"]
sslmode = "require"
table_name = os.environ["DB_TABLE_NAME"]

# Weather API variables
api_base_url = os.environ["WEATHER_API_BASE_URL"]
api_parameters = os.environ["WEATHER_API_PARAMETERS"]
api_key = os.environ["WEATHER_API_KEY"]
api_url = api_base_url + api_parameters + '&key=' + api_key
