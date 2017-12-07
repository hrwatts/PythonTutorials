#sql_basics.py
#based on a course I got from DataCamp.com "Introduction to Databases in Python"
#SQLAlchemy basics, connections, reflection objects

#create_engine is what you use to connect with a database
from sqlalchemy import create_engine, MetaData, Table

#supply create_engine() with a string that represents the connection URL
#this is what the connection URL looks like
# dialect+driver://username:password@host:port/database
#what this means is
#dialect = what kind of SQL DB is it? MS SQL, MySQL, PostGRE, etc.
#driver = SQLAlchemy runs over other python packages so that the end user (me) can use
#a common interface between them. The python connector MySQL offers, is what I'll use
#also, don't put your passwords online

#to be able to run this, use the pets.sql file to make a simple test DB on your local host

engine = create_engine("mysql+mysqlconnector://USERNAME:PASSWORD@localhost/pets")

#and then to make connections to the DB you need to do this
#it is worth noting that it won't actually make a connection until it is being used
connection = engine.connect() #connection made like this, for testing

#you'll use the engine conceptually like your database
#let's see what tables are in our DB
print(engine.table_names())

#you want to work without the server as much as you can, considering the speed of calculations
#would be awful. So what we do is build a python object on our end that mirrors the DB
#this is called reflection, and it will allow us to stop making connections to use data

#initialize, just to make it easier to read the code
#MetaData is all the info about what kind of data is stored in a table
metadata = MetaData()

#this is our reflected object, essentially is is the cats table in the DB, except in our local memory
#autoload allows us to go ahead and make the connection now to load this reflected table
cats = Table('cats', metadata, autoload=True, autoload_with=engine)

#note: the defualt print out of a Table is terrible
print(cats)
print(type(cats))

#use repr() function to get an informative print out
#repr() just is an advanced object printing function in python 
#that returns printable representation of an object
print(repr(cats))
