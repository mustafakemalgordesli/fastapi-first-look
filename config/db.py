from sqlalchemy import ForeignKey, create_engine, Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime
from sqlalchemy.orm import relationship



engine = None
Session = None
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column('id', Integer, primary_key=True)
    email = Column('email', String, unique=True, nullable=False)
    firstName = Column('firstName', String, nullable=False)
    lastName = Column('lastName', String, nullable=False)
    password = Column('password', String, nullable=False)
    createdAt = Column('createdAt', DateTime) 
    updatedAt = Column('updatedAt', DateTime)
    status = Column('status', Boolean, nullable=False)
    
    
    class Config:
        orm_mode = True
        
    # def __init__(self, **kwargs):
    #     super(User, self).__init__(**kwargs)
    
    # def __init__(self, email, firstName, lastName, password):
    #     self.id = 0
    #     self.email = email
    #     self.firstName = firstName
    #     self.lastName = lastName
    #     self.password = password
    #     self.status = True
    #     self.createdAt = datetime.datetime.now()
    
    
# class Todo(Base):
#     __tablename__ = "todos"
#     id = Column('id', Integer, primary_key=True)
#     todo = Column("todo", String, nullable=False)
#     deadline = Column("deadline", DateTime)
#     createdAt = Column('createdAt', DateTime, nullable=False) 
#     updatedAt = Column('updatedAt', DateTime)
#     isCompleted = Column('isCompleted', Boolean, nullable=False)
#     isDeleted = Column('isDeleted', Boolean, nullable=False)
#     user_id = Column(Integer, ForeignKey("users.id"))
#     user = relationship("User", back_populates="todos")
    
#     def __init__(self, todo, deadline, user_id):
#         self.id = 0
#         self.deadline = deadline 
#         self.todo = todo
#         self.user_id = user_id
#         self.createdAt = datetime.datetime.now()
#         self.isCompleted = False,
#         self.isDeleted = False

try:    
    engine = create_engine('mysql+pymysql://root:@localhost/testdb', pool_size=10, max_overflow=20)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
except Exception as e:
    print(e)



