class Job:
    def __init__(self):
        self.ref = ""
        self.title = ""
        self.salary = ""
        self.loc = ""
        self.type = ""
        self.when = ""
        self.skills = ""
        self.duration = ""
        self.start_date = ""
        self.rate = ""
        self.recruiter = "" 
        self.posted_date = ""
        self.permalink = ""
    
    def __str__(self):
        return (
            f"Job Title: {self.title}\n"
            f"Salary: {self.salary}\n"
            f"Location: {self.loc}\n"
            f"Type: {self.type}\n"
            f"When: {self.when}\n"
            f"Skills: {self.skills}\n"
            f"Duration: {self.duration}\n"
            f"Start Date: {self.start_date}\n"
            f"Rate: {self.rate}\n"
            f"Recruiter: {self.recruiter}\n"
            f"Reference: {self.ref}\n"
            f"Posted Date: {self.posted_date}\n"
            f"Permalink: {self.permalink}"
        )