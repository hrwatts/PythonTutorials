#census3.py
#based on a course I got from DataCamp.com "Introduction to Databases in Python"
#SQLite, Aggregation, Distinct, Group By

from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy import select, or_, and_, not_, desc
from sqlalchemy import func #to use .sum() and .count() don't import those directly, python conflicts

#connect to DB
engine = create_engine("sqlite:///census.sqlite")
connection = engine.connect()

#set up metadata
metadata = MetaData()

#get the table (there is only one in census.sqlite)
census = Table('census', metadata, autoload=True, autoload_with=engine)

#you can use .distinct() which is an SQL command, to only grab distinct values
stmt = select([census.columns.state.distinct()])
stmt = stmt.order_by(census.columns.state)
results = connection.execute(stmt).fetchall()
print("All States:"+'*'*77+"\n",results)

#there are some operations you can do in SQL that are more efficient than doing them in python
#examples: Count, Sum
#these two are called aggregation functions, cause they collapse multiple records into one
#to use it in an SQLAlchemy select query, do this
stmt = select([func.sum(census.columns.pop2008)])

#execute the query and get the results from a ResultProxy
results = connection.execute(stmt).fetchall()

print("Sum of US population from the census 2008:",results, 30*'*')

#alternatively, since we know only one value is coming back from this query
#we can use .scalar() instead of .fetch() methods, it will return just the value, not RowProxy
results = connection.execute(stmt).scalar()
print("Scalar Sum of US population from the census 2008:",results, 28*'*')

#you can also use SQL "Group By" statements with aggregate functions
#Group By is done almost exaclt the same as Order By
#if using multiple columns to group by, it will do them left to right like order by
#To use .group_by() the columns must be selected, and must have been grouped or aggregated
stmt = select([census.columns.sex, func.sum(census.columns.pop2008)])
stmt = stmt.group_by(census.columns.sex)
results = connection.execute(stmt).fetchall()
print("2008 Population Grouped By Sex:",results, "*"*19)

#huh, slightly more females than males for the US in 2008

#let's demo the multiple group by by grouping population by sex and age
#columns must be selected
stmt = select([census.columns.sex, census.columns.age, census.columns.pop2008])
stmt = stmt.group_by(census.columns.sex, census.columns.age)
switch=True
print("2008 US Population grouped by Sex and Age:" + "*"*46)
for result in connection.execute(stmt):
	if result[0]!='F' and switch:
		print("Male Population by Age " + "*"*20)
		switch = False
	print(result)

#SQLAlchemy uses place holders for newly generated columns (such as an aggregate of a column)
#this makes it somewhat unintuitive to use at first
stmt = select([census.columns.sex, func.sum(census.columns.pop2008)])
stmt = stmt.group_by(census.columns.sex)
results = connection.execute(stmt).fetchall()
print("Result Keys with Place Holder",results[0].keys(), '*'*30) #remember RowProxys have .keys() not ResultSets

#we see that sum_1 is given for the sum of pop2008
#so if we want to give it a meaningful name, use .label() 
#to let it know what to change place holder to during the aggregate function
stmt = select([census.columns.sex, func.sum(census.columns.pop2008).label('pop2008_sum')])
stmt = stmt.group_by(census.columns.sex)
results = connection.execute(stmt).fetchall()
print("Result Keys Labelled",results[0].keys(),"*"*33)


