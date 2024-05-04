# Executing inside a Docker container
# SELECT: "vs-code-ubuntu" or "docker" if executing inside VS Code Terminal Ubuntu or outside VS Code in Docker
import json

CURRENT_COMPUTER = "powershell"
BASE_FOLDER_DICT = {
    "vs-code-ubuntu": "./", 
    "powershell": ".\\"
    }

BASE_FOLDER =  BASE_FOLDER_DICT[CURRENT_COMPUTER]
DATA_FOLDER = BASE_FOLDER + "/data"

JOBS_DATABASE_NAME = f"job-scrape"
JOBS_DATABASE_PATH_NAME = f"{DATA_FOLDER}/{JOBS_DATABASE_NAME}.db"

DATABASE_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

def get_secret(key: str):
    with open(BASE_FOLDER + "config.json", "r") as config_file:
        config = json.load(config_file)
        secret_value = config[f"{key}"]
    return secret_value