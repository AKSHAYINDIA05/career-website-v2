import os
from sqlalchemy import create_engine, text

my_secret = os.environ['connection_db_new_user']

engine = create_engine(my_secret,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})

# def load_jobs_from_db():
#   with engine.connect() as conn:
#     result = conn.execute(text("select * from codeasy.jobs"))
#     jobs = []
#     for row in result.all():
#       jobs.append(row._mapping)
#     return jobs


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs"))
    jobs = []
    for row in result.fetchall():
      job = {}
      for idx, column in enumerate(result.keys()):
        job[column] = row[idx]
      jobs.append(job)
    return jobs


def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs where id=:job_id"),
                          {"job_id": id})
    rows = result.fetchall()
    if len(rows) == 0:
      return None
    else:
      return rows[0]._mapping


# def add_application_to_db(job_id, data):
#   with engine.connect() as conn:
#     query = text(
#       "insert into applications (job_id, full_name, number, email, linkedin, education , experience, resume) values (:job_id, :full_name, :number, :email, :linkedin, :education, :experience, :resume)"
#     )
#     conn.execute(query,
#                  job_id=job_id,
#                  full_name=data['full_name'],
#                  email=data['email'],
#                  number=data['number'],
#                  linkedin=data['linkedin'],
#                  education=data['education'],
#                  experience=data['experience'],
#                  resume=data['resume'])


def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    query = text(
      "insert into applications (job_id, full_name, email, number, linkedin, education , experience, resume) values (:job_id, :full_name, :email, :number,:linkedin, :education, :experience, :resume)"
    )
    params = {
      'job_id': job_id,
      'full_name': data['full_name'],
      'email': data['email'],
      'number': data['number'],
      'linkedin': data['linkedin'],
      'education': data['education'],
      'experience': data['experience'],
      'resume': data['resume']
    }
    conn.execute(query, params)
