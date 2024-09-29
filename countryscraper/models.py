from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

#change the "username" and "password" with your mysql credentials
def db_connect():
    return create_engine('mysql+pymysql://admin:germany2024@localhost/countryscraper')

def create_table(engine):
    Base.metadata.create_all(engine)

class Country(Base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    capital = Column(String(255))
    population = Column(Integer)
    area = Column(Float)
