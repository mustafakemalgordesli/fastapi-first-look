from ast import Try
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = None
Session = None
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column('id', Integer, primary_key=True)
    email = Column('email', String, unique=True)
    firstName = Column('firstName', String)
    lastName = Column('lastName', String)
    password = Column('password', String)
    status = Column('status', Boolean)

try:    
    engine = create_engine('mysql+pymysql://root:@localhost/testdb', pool_size=10, max_overflow=20)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
except Exception as e:
    print(e)



