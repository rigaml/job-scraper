from pydantic import BaseModel

from services.job_dto import JobDTO


class JobResponse(BaseModel):

    ref: str = ""
    title: str = ""
    salary: str = ""
    loc: str = ""
    job_type: str = ""
    skills: str = ""
    duration: str = ""
    start_date: str = ""
    rate: str = ""
    recruiter: str = ""
    posted_date: str = ""
    permalink: str = ""

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
    def create_from_dto(cls, job: JobDTO):
        return cls(job.ref, job.title, job.salary, job.loc, job.title, job.skills, job.duration,
                   job.start_date, job.rate, job.recruiter, job.posted_date, job.permalink)
