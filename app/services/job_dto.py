"""
Job scraped from the website.
"""


from database.job import Job


class JobDTO:
    """
    Job Data Transfer Object
    """

    def __init__(self,
                 ref: str = "",
                 title: str = "",
                 salary: str = "",
                 loc: str = "",
                 job_type: str = "",
                 skills: str = "",
                 duration: str = "",
                 start_date: str = "",
                 rate: str = "",
                 recruiter: str = "",
                 posted_date: str = "",
                 permalink: str = ""):
        self.ref = ref
        self.title = title
        self.salary = salary
        self.loc = loc
        self.type = job_type
        self.skills = skills
        self.duration = duration
        self.start_date = start_date
        self.rate = rate
        self.recruiter = recruiter
        self.posted_date = posted_date
        self.permalink = permalink

    @classmethod
    def create_from_db(cls, job: Job):
        return cls(job.ref, job.title, job.salary, job.location, job.title, job.skills, job.duration,
                   job.start_date, job.rate, job.recruiter, job.posted_date, job.permalink)

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