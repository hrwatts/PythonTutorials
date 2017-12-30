#census6.py
#based on a course I got from DataCamp.com "Introduction to Databases in Python"
#SQLite, Joins, Foreign Keys

import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy import select, or_, and_, not_, desc
from sqlalchemy import func, desc
from sqlalchemy import case, cast, Float

#connect to DB
engine = create_engine("sqlite:///census.sqlite")
connection = engine.connect()

#set up metadata
metadata = MetaData()

#get the desired table, and build reflection object
#if you don't know the names of the tables use engine.table_names()
census = Table('census', metadata, autoload=True, autoload_with=engine)
state_fact = Table('state_fact', metadata, autoload=True, autoload_with=engine)

#joins are what you use to go between two different tables
#SQLAlchemy can do it automatically using the foreign key in many cases
stmt = select([func.sum(census.columns.pop2008), state_fact.columns.abbreviation])
stmt = stmt.group_by(state_fact.columns.abbreviation)
results = connection.execute(stmt).fetchall()
[print(x) for x in results]

#this displayed data from two tables (though, not very nicely...)
#SQLAlchemy was able to join them automatically due to a predefined relationship (foreign key)
#you can set a relationship that isn't already defined though
#it always goes immediately after the select() clause, 
#and before any where(), order_by() or group_by() clause
#we can use a select_from() clause (which is derived from the FROM clause)
#to let SQLAlchemy know what tables we actually want to use

#let's make a more advanced query
#total population in 2008 within the bounds of the 10th federal circuit court
stmt = select([func.sum(census.columns.pop2008)]) #all we want returned is population

#join it with state_fact since that's where the circuit court info is
#NOTE: if relationship is predefined (foreign keys) you don't need to specify
#but if it is NOT then just add the condition by which you want to join the two tables
#by two columns. They must be of the same type
stmt = stmt.select_from(census.join(state_fact, census.columns.state==state_fact.columns.name)) 

#now we can specify additional things, since we are working with the joined tables
stmt = stmt.where(state_fact.columns.circuit_court=='10')

#it's just one number (the population) so fetch it as so
result = connection.execute(stmt).scalar()

print("Population from 10th Circuit Court 2008:",result, '*'*30)
