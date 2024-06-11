"""
Configuration values and utility to get configuration values.
"""

import json

DATA_FOLDER = "data"
JOBS_DATABASE_NAME = "job-scrape"
JOBS_DATABASE_PATH_NAME = f"{DATA_FOLDER}/{JOBS_DATABASE_NAME}.db"

DATABASE_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

SCRAPE_SITE = "jobserve"

# Set SCRAPE_SHOW_BROWSER to True if want to see what the scapting process is doing.
# Note for this to work the environment which runs the application should have a
# graphical interface to execute Chrome browser
SCRAPE_SHOW_BROWSER = False

# Maximum number of jobs retrieved from the targeted web page
SCRAPE_RETRIEVE_MAX = 30


def get_secret(key: str):
    """
    Retrieves a secret value from the configuration file.
    Raises:
        KeyError: If the provided key is not found in the configuration file.
    """
    with open("./app/config.json", "r", encoding="utf-8") as config_file:
        config = json.load(config_file)
        secret_value = config[f"{key}"]
    return secret_value
