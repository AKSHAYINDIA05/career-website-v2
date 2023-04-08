import os
from sqlalchemy import create_engine, text
my_secret = os.environ['connection_db']

engine = create_engine(my_secret,
  connect_args={"ssl": {
    "ssl_ca": "/etc/ssl/cert.pem"
  }})

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from codeasy.jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._mapping)
    return jobs

