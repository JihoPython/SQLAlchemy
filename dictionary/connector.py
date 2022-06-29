from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# engine = create_engine('postgresql://postgres:jiho0614@localhost:5432/alchemy', echo=False)
engine = create_engine('mysql+pymysql://root:jiho0614@localhost:3306/school', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
