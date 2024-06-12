from typing import List
from faker import Faker

from app.services.job_dto import JobDTO

fake = Faker()

def generate_job_dtos(count: int) -> List[JobDTO]:
    return [
        JobDTO(
            ref=fake.uuid4(),
            title=fake.sentence(),
            salary=f'£{fake.random_int(min=10000, max=100000)}',
            loc=fake.city(),
            job_type=fake.word(),
            skills=' '.join(fake.words(nb=3)),
            duration=str(fake.random_int(min=1, max=12)),
            start_date=fake.date_this_year().strftime('%Y-%m-%d'),
            rate=f'£{fake.random_int(min=10, max=100)}/hour',
            recruiter=fake.name(),
            posted_date=fake.date_this_year().strftime('%Y-%m-%d'),
            permalink=fake.url()
        )
        for _ in range(count)
    ]
