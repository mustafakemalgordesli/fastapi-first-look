from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column('id', Integer, primary_key=True)
    email = Column('email', String, unique=True)
    firstName = Column('firstName', String)
    lastName = Column('lastName', String)
    password = Column('password', String)
    status = Column('status', Boolean)

engine = create_engine('mysql+pymysql://root:@localhost/testdb', echo=True)

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)


