from sqlalchemy import create_engine, text

engine = create_engine(f'mysql+pymysql://hyy37wxipb3wz7mccw1c:pscale_pw_zahW4crsS3pvu30mm3fSH9umPYD8arHAj2jGLjZwZay@aws.connect.psdb.cloud/codeasy',
                       connect_args={
                        "ssl":{
                            "ssl_ca":"/etc/ssl/cert.pem"
                        }
                       })

with engine.connect() as conn:
    result = conn.execute(text("select * from codeasy.jobs"))
    result_dicts = []
    for row in result.all():
        result_dicts.append(row._mapping)
    print(result_dicts)