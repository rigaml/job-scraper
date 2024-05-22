"""
Job scraped from the website.
"""


class Job:
    """Job fields"""

    def __init__(self):
        self.ref = ""
        self.title = ""
        self.salary = ""
        self.loc = ""
        self.type = ""
        self.skills = ""
        self.duration = ""
        self.start_date = ""
        self.rate = ""
        self.recruiter = ""
        self.posted_date = ""
        self.permalink = ""

    def __str__(self):
        return (
            f"Job(ref= {self.ref}, "
            f"title= {self.title}, "
            f"salary= {self.salary}, "
            f"loc= {self.loc}, "
            f"type= {self.type}, "
            f"skills= {self.skills}, "
            f"duration= {self.duration}, "
            f"start_date= {self.start_date}, "
            f"rate= {self.rate}, "
            f"recruiter= {self.recruiter}, "
            f"posted_date= {self.posted_date}, "
            f"permalink= {self.permalink})"
        )
