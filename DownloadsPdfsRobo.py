import os
import json
import requests
from urllib.parse import urlparse

# Create directory to save files if it doesn't exist
folder_path = './arquivos/2015'
os.makedirs(folder_path, exist_ok=True)

# Path to the JSON file
json_file_path = './arquivos/dissertação-2015.json'

# Function to download files
def download_file(url, file_name):
    try:
        response = requests.get(url)
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"File '{file_name}' downloaded successfully.")
    except Exception as e:
        print(f"Error downloading file '{file_name}': {str(e)}")

# Read the JSON file
try:
    with open(json_file_path, 'r') as file:
        url_list = json.load(file)
except Exception as e:
    print(f"Error reading JSON file: {str(e)}")
    url_list = []

# Download files from URLs
for url in url_list:
    file_name = os.path.join(folder_path, os.path.basename(urlparse(url).path))
    download_file(url, file_name)
