#sql_basics.py
#based on a course I got from DataCamp.com "Introduction to Databases in Python"
#SQLAlchemy basics

#create_engine is what you use to connect with a database
from sqlalchemy import create_engine

#supply create_engine() with a string that represents the connection
engine = create_engine("")

#and then to make connections to the DB you need to do this
#it is worth noting that it won't actually make a connection until it is being used
connection = engine.connect()
