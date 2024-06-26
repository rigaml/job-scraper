# Job Vacancy Web Scraping Project

## Overview

Demo project to practice Python and Machine Learning technologies.

Project extracts job posting from jobs sites and analizes the data.

## Prerequisites

Python 3.6 or higher.

See `requirements.txt` in the folder.

## Getting Started (Linux/Unix instructions)

1. **Clone this repo from GitHub:**
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

5. **Navigate to the application folder:**

```bash
    cd app
```

6. **Set the PYTHONPATH environment variable:**

```bash
    export PYTHONPATH="./"
```

7. **First time database setup: create SQLite database to store the jobs:**

```bash
    python scripts/create_database.py
```

8. **Create a directory to store logs:**

```bash
    mkdir ../logs
```

9. **Execute program to scrape jobs(first see "Set job search parameters"):**

```bash
    python scrape_jobs.py
```

### Set job search parameters:

Currently only scraped site is [Jobserve](https://www.jobserve.com/). If you are interested in a particular set of jobs to store in the database you can populate the Jobserve Job Search form and perform your search. Then use the session Id (shid) that appear in the browser querystring to target these set. To do this, follow the steps:

1. Go to `https://www.jobserve.com/gb/en/Job-Search/` and set the values for your job search in the search form.
2. After hitting Search button, you will redirected to a search results page.
3. From the URL you can obtain the `session-id` value `https://www.jobserve.com/gb/en/JobSearch.aspx?shid=<session-id>`
4. Use the `config-base.json` to populate the value of the `shid`

```json
{
  "jobserve-shid": "<session-id>"
}
```

5. Rename this `config-base.json` to `config.json`

NOTE: After few days not accessing Jobserve with this `session-id`, it will expire and you will need to repopulate the search as explained in previous steps.

**Additional Notes**:

- Ensure you have Python 3.6 or higher installed on your system.
- Run the unit test from the `app` folder executing `pytest`.
- Check the logs in the `../logs` directory if you encounter any issues running the application.

Build the Docker Image

```
docker build -t scrapejobs .
```

Run the Docker Container

```
docker run -p 8000:80 scrapejobs
```

Inspect the application endpoints from the browser with

```
http://127.0.0.1:8000/docs
```

Execute on WSL or Docker container
https://stackoverflow.com/questions/75012949/how-to-run-chrome-headless-in-docker-container-with-selenium

wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb

CHROME_VERSION=$(google-chrome --version | cut -d ' ' -f 3 | cut -d '.' -f 1)
For chromedriver-linux64.zip go to https://googlechromelabs.github.io/chrome-for-testing/
and install same version you have in echo $CHROME_VERSION
unzip chromedriver-linux64.zip
go inside the folder where you unzipped /chromedriver-linux64
and move the chromedriver as below
sudo mv chromedriver /usr/bin/chromedriver
sudo chmod +x /usr/bin/chromedriver

https://sites.google.com/chromium.org/driver/downloads
If you are using Chrome version 115 or newer, please consult the Chrome for Testing availability dashboard. This page provides convenient JSON endpoints for specific ChromeDriver version downloading.

## Project Structure

- [Outline the project's file structure and explain the purpose of each file/directory]

## Data Source

[Specify the job posting site you chose for web scraping and provide a brief justification for your choice. If you encountered any anti-scraping filters, mention how you handled them.]

Scraping jobs advertisements from [JobServe](https://www.jobserve.com/) site.

## Data Processing

[Explain the steps involved in processing the scraped data, such as cleaning, transforming, or filtering the data.]

## Analysis and Visualization

[Describe the techniques and tools you used for analyzing and visualizing the data. You can include sample visualizations or screenshots in this section.]

## Findings and Recommendations

[Summarize your key findings and provide recommendations based on your analysis. This section should highlight the insights gained from the project and how they can help the recruitment agency achieve its objectives.]

## Limitations and Future Improvements

[Discuss any limitations or challenges you faced during the project and suggest potential improvements or future enhancements.]

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
