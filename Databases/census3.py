#census3.py
#based on a course I got from DataCamp.com "Introduction to Databases in Python"
#SQLite, Aggregation

from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy import select, or_, and_, not_, desc
from sqlalchemy import func

#connect to DB
engine = create_engine("sqlite:///census.sqlite")
connection = engine.connect()

#set up metadata
metadata = MetaData()

#get the table (there is only one in census.sqlite)
census = Table('census', metadata, autoload=True, autoload_with=engine)

#there are some operations you can do in SQL that are more efficient than doing them in python
#examples: Count, Sum
#these two are called aggregation functions, cause they collapse multiple records into one
#to use it in an SQLAlchemy select query, do this
stmt = select([func.sum(census.columns.pop2008)])

#execute the query and get the results from a ResultProxy
results = connection.execute(stmt).fetchall()

print("Sum of US population from the census 2008:",results, 30*'*')
