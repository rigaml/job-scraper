# Job Vacancy Web Scraping Project

## Overview

Demo project to play with few machine learning technologies.

Code automatically extracts job posting data from posting sites and analizes the data.

## Prerequisites

This project contains `Jupyter Notebooks` to rapid testing of different scenarios.

See `requirements.txt` in the folder.

## Getting Started

1. [Provide instructions on how to set up the project environment]
2. [Explain how to run the web scraping script]
3. [Describe any additional steps needed to execute the project]

<!-- Comment forces a numbering re-start of list below -->

### Set job search parameters:

1. Go to `https://www.jobserve.com/gb/en/Job-Search/` and set the values for your job search in the search form.
2. After hitting Search button, you will redirected to a search results page.
3. From the URL you can obtain the `session-id` value `https://www.jobserve.com/gb/en/JobSearch.aspx?shid=<session-id>`
4. Add it to a `config.json` in the application base folder.

```json
{
  "jobserve-shid": "<session-id>"
}
```

NOTE: After few days of not using this `session-id` it will expire and then will need repeat the previous steps

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

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Acknowledgements

[Optionally, you can acknowledge any resources, libraries, or individuals who contributed to the project.]
