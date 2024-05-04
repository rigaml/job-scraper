import time
from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from scrapers.base_scraper import BaseScrapper
from models.job import Job

import utilities.text_utils as text_utils
import utilities.html_utils as html_utils


class JobServeScraper(BaseScrapper):
    JOBS_URL = "https://www.jobserve.com/gb/en/JobSearch.aspx?shid="

    def __init__(self, session_id, show_browser= False):
        self.jobs_url = self.JOBS_URL + session_id
        super().__init__(self.jobs_url, show_browser)

    def scrape_jobs(self, retrieve_jobs_max: int, print_trace= False) -> List[Job]:
        # Selector list of offers
        sel_job_list = '#jsJobResContent .jobItem'
        
        # Selectors fields for each item in the list of offers
        sel_job_item_title = '.jobResultsTitle'
        sel_job_item_salary = '.jobResultsSalary'
        sel_job_item_loc = '.jobResultsLoc'
        sel_job_item_type = '.jobResultsType'
        sel_job_item_when = '.when'

        # Selector job details container
        sel_job_detail_container = "#JobDetailContainer .jsCustomScrollContainer"

        # Job details description
        sel_job_detail_skills = '#md_skills'
        sel_job_detail_duration = '#md_duration'
        sel_job_detail_start_date = '#md_start_date'
        sel_job_detail_rate = '#md_rate'
        sel_job_detail_recruiter = '#md_recruiter'
        sel_job_detail_ref = '#md_ref'
        sel_job_detail_posted_date = '#md_posted_date'
        sel_job_detail_permalink = '#md_permalink'

        # Find all job offer items in the list
        job_items = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, sel_job_list)))
        
        if print_trace: print(f"Job_tems found: {len(job_items)} and max required: {retrieve_jobs_max}")
        
        job_items = job_items[: min(len(job_items), retrieve_jobs_max)]
        retrieved_jobs = []

        for index, job_item in enumerate(job_items):
            if print_trace: print(f"**Job Index: {index + 1}")

            # Click on the job item to load its details into the div; text outside the view can't be seen by Selenium
            ActionChains(self.driver).move_to_element(job_item).click(job_item).perform()
            time.sleep(2)

            current_job= Job()
            # Extract fields in job item section
            current_job.title = html_utils.find_element_or_none(job_item, sel_job_item_title)
            current_job.salary = html_utils.find_element_or_none(job_item, sel_job_item_salary)
            current_job.loc = html_utils.find_element_or_none(job_item, sel_job_item_loc)
            current_job.type = html_utils.find_element_or_none(job_item, sel_job_item_type)
            current_job.when = html_utils.find_element_or_none(job_item, sel_job_item_when)
            
            # Select the job detail section
            job_detail_container = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, sel_job_detail_container)))

            # Get the scrollable height of the detail container 
            scroll_height = self.driver.execute_script("return arguments[0].scrollHeight;", job_detail_container)
            if print_trace: print(f"scroll_height: {scroll_height}")

            current_scroll_position = 0
            increase = 100
            # As selenium only retrieve the visible area then scroll to get every bit of text
            while current_scroll_position < scroll_height:
                self.driver.execute_script(f"arguments[0].style.top = '-{current_scroll_position}px';", job_detail_container)
                current_scroll_position += increase
                # Wait for some time to allow content to load (you may adjust the time as needed)
                time.sleep(1)
                
                skills_try = html_utils.find_element_or_none(job_detail_container, sel_job_detail_skills)
                current_job.skills = text_utils.join_without_overlap(current_job.skills, skills_try)
                duration_try = html_utils.find_element_or_none(job_detail_container, sel_job_detail_duration)
                current_job.duration = text_utils.join_without_overlap(current_job.duration, duration_try)
                start_date_try = html_utils.find_element_or_none(job_detail_container, sel_job_detail_start_date)
                current_job.start_date = text_utils.join_without_overlap(current_job.start_date, start_date_try)
                rate_try = html_utils.find_element_or_none(job_detail_container, sel_job_detail_rate)
                current_job.rate = text_utils.join_without_overlap(current_job.rate, rate_try)
                recruiter_try = html_utils.find_element_or_none(job_detail_container, sel_job_detail_recruiter)
                current_job.recruiter = text_utils.join_without_overlap(current_job.recruiter, recruiter_try)
                ref_try = html_utils.find_element_or_none(job_detail_container, sel_job_detail_ref)
                current_job.ref = text_utils.join_without_overlap(current_job.ref, ref_try)
                posted_date_try = html_utils.find_element_or_none(job_detail_container, sel_job_detail_posted_date)
                current_job.posted_date = text_utils.join_without_overlap(current_job.posted_date, posted_date_try)
                permalink_try = html_utils.find_element_or_none(job_detail_container, sel_job_detail_permalink)
                current_job.permalink = text_utils.join_without_overlap(current_job.permalink, permalink_try)

            if print_trace: 
                print(f"{index + 1}-Item\ntitle:{current_job.title}\nsalary:{current_job.salary}\nloc:{current_job.loc}\ntype:{type}\nwhen:{current_job.when}\n")
                print(f"{index + 1}-Details\nskills:{current_job.skills}\nduration:{current_job.duration}\nstart_date:{current_job.start_date}\nrecruiter:{current_job.recruiter}\nref:{ref}\nposted_date:{current_job.posted_date}\npermalink:{current_job.permalink}\n")

            retrieved_jobs.append(current_job)                

            return retrieved_jobs


