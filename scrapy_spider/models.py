
from scrapy.utils.project import get_project_settings

# from sqlalchemy import create_engine, Column, Table, ForeignKey
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import (
#     Integer, SmallInteger, String, Date, DateTime, Float, Boolean, Text, LargeBinary)


# DeclarativeBase = declarative_base()

# def db_connect():
#     """
#     Performs database connection using database settings from settings.py.
#     Returns sqlalchemy engine instance
#     """
    
#     return create_engine(get_project_settings().get("CONNECTION_STRING"))

# def create_table(engine):
#     DeclarativeBase.metadata.create_all(engine)

# class OoyyoDB(DeclarativeBase):
#     __tablename__ = "ooyyo_table"

#     id = Column(Integer, primary_key=True)
#     ooyyo = Column('ooyyo', Text())
#     author = Column('author', String(100))

