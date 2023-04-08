from sqlalchemy import create_engine, text

engine = create_engine(
  f'mysql+pymysql://qbjsdkn7ipqpuu1sj94j:pscale_pw_4Hlo3ppH5SqMPEp0syuG3Ibp3JPg14CVkaVC6oFCDP6@aws.connect.psdb.cloud/codeasy',
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

