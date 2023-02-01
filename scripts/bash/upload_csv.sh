#!/usr/bin/env bash
set -e
set -o pipefail

SCRIPT_PATH="$(dirname "${BASH_SOURCE[0]}")"

# Login to Azure with Service Principal
echo 'Login to Azure'
if [ "$(az login \
    --service-principal \
    --username "${AZURE_CLIENT_ID}" \
    --password "${AZURE_CLIENT_SECRET}" \
    --tenant "${AZURE_TENANT_ID}")" ]; then
    echo "Logged in"
    else
    echo "Login failed, go fix it!!"
    exit 1
fi

# Upload the csv file to the container
echo 'Upload csv file'
if [ "$(az storage blob upload --account-name "${AZURE_STORAGE_ACCOUNT_NAME}" \
    --account-key "$(az storage account keys list --account-name "${AZURE_STORAGE_ACCOUNT_NAME}" --query "[0].value" --output tsv)" \
    --container-name "${AZURE_STORAGE_CONTAINER_NAME}" \
    --type block \
    --file "${SCRIPT_PATH}/../../data/${CSV_FILENAME}" \
    --name "${CSV_FILENAME}")" ]; then
    echo "Csv uploaded"
    else
    echo "Csv upload failed, go fix it!!"
    exit 1
fi
