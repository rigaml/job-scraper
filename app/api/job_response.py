from pydantic import BaseModel, Field

from app.services.job_dto import JobDTO


class JobResponse(BaseModel):

    ref: str = Field(default="")
    title: str = Field(default="")
    salary: str = Field(default="")
    loc: str = Field(default="")
    type: str = Field(default="")
    skills: str = Field(default="")
    duration: str = Field(default="")
    start_date: str = Field(default="")
    rate: str = Field(default="")
    recruiter: str = Field(default="")
    posted_date: str = Field(default="")
    permalink: str = Field(default="")


    @classmethod
    def create_from_dto(cls, job: JobDTO) -> 'JobResponse':
        return cls(ref=job.ref, title=job.title, salary=job.salary, loc=job.loc, type=job.type, skills=job.skills, duration=job.duration,
                   start_date=job.start_date, rate=job.rate, recruiter=job.recruiter, posted_date=job.posted_date, permalink=job.permalink)

    def __repr__(self):
        return (
            f"JobResponse("
            f"ref='{self.ref}', "
            f"title='{self.title}', "
            f"salary='{self.salary}', "
            f"loc='{self.loc}', "
            f"type='{self.type}', "
            f"skills='{self.skills}', "
            f"duration='{self.duration}', "
            f"start_date='{self.start_date}', "
            f"rate='{self.rate}', "
            f"recruiter='{self.recruiter}', "
            f"posted_date='{self.posted_date}', "
            f"permalink='{self.permalink}'"
            ")"
        )