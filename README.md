# Job Vacancy Web Scraping Project

## Overview

Demo project to practice Python and Machine Learning technologies.

Project extracts job posting from jobs sites and analizes the data.

## Prerequisites

Python 3.7+ (as it used @dataclass decorator).

See `requirements.txt` in the folder.

## Getting Started (Linux/Unix instructions)

1. **Clone this repo from GitHub**

Open a terminal window in repo's root folder and follow the steps below

2. **Create a Python virtual in the folder that contains this repo:**

```bash
    python -m venv venv
```

3. **Activate the virtual environment:**

```bash
    source venv/bin/activate
```

4. **Install the project dependencies:**

```bash
    pip install --no-cache-dir --upgrade -r requirements.txt
```

5. **Set the PYTHONPATH environment variable:**

```bash
    export PYTHONPATH="./"
```

6. **First time database setup: create SQLite database to store the jobs:**

```bash
    python app/scripts/create_database.py
```

7. **Create a directory to store logs:**

```bash
    mkdir logs
```

8. **Execute program to scrape jobs(first see "Set job search parameters"):**

```bash
    python app/scrape_jobs.py
```

### Start API for local development
Open a terminal window in repo's root folder and start the API for local development

```bash
    fastapi dev app/main.py
```
Once it starts, open a browser window and enter `http://127.0.0.1:8000/docs` to try the endpoints on Swagger.

### Unit test
Open a terminal window in repo's root folder and execute
```bash
    pytest
```

### Set job search parameters:

Currently only scraped site is [Jobserve](https://www.jobserve.com/).

If you are interested in a particular set of jobs to store in the database you can populate the Jobserve search form. Then use the session Id (shid) that appear in the browser querystring to target these set from the application. To do this, follow the steps:

1. Go to `https://www.jobserve.com/gb/en/Job-Search/` and fill the search form with your requirements.
2. After hitting Search button, you will be redirected to a search results page.
3. From the URL you can obtain the session id `shid` value: `https://www.jobserve.com/gb/en/JobSearch.aspx?shid=<session-id>`
4. In the `.env` file to add a line with JOBSERVE-SHID= the `shid` got in the URL

```plaintext
JOBSERVE-SHID=<session-id>
```

NOTE: After 2 days not accessing Jobserve with this session id, it will expire and you will need to repopulate the search as explained in previous steps.

**Additional Notes**:

- Check the logs in the `../logs` directory if you encounter any issues running the application.
- Jobs scraped are stored in the SQLite database `data/job-scrape.db`. Install a SQLite browser to inspect data retrieved. There are some SQL queries `queries.sql` file.

## Limitations and Future Improvements

- Add web interface to extract insights from the database.
- Application to set particular values in the Search form to avoid having to deal with the expired session id.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
