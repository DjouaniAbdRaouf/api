from sqlalchemy import create_engine , MetaData

engine = create_engine("mysql+pymysql://root@localhost:8000/dbfastapi")
meta = MetaData()
db = engine.connect()