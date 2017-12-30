#census5.py
#based on a course I got from DataCamp.com "Introduction to Databases in Python"
#SQLite, Math Operators, Case Statements

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

#get the table (there is only one in census.sqlite)
census = Table('census', metadata, autoload=True, autoload_with=engine)

#Math operators are things line +,-,*,/, and %
#to use them in an SQLAlchemy query, you literally just type them out
#it is notable to say they don't work the same way when using non-numeraic data types

#let's say we want to see the growth in population between 2000 and 2008 in our DB
#just to reiterate the process, you pass select a list as an argument for what you want returned
#so we want the age group, along with a new column made by subtracting pop2000 from pop2008
#and we want this new column to not go by SQLAlchemy's defualt naming system, but by 'growth'
#we do this here because SQL will be able to process the request faster than doing it locally
#so these calculations would be done server-side.
stmt = select([census.columns.age, (census.columns.pop2008 - census.columns.pop2000).label('growth')])

#group the results by age group, that is, for all 50 states
#by modifying the select query
stmt = stmt.group_by(census.columns.age)

results = connection.execute(stmt).fetchall()

print("US Population Growth by Age Group 2000-2008", '*'*30)
[print(x[0],x[1]) for x in results]

#we can modify this further to get the top 5 age groups in population growth
#we just order it by 'growth'1733
#and .limit() it to 5, so we won't actually fetch any more even if we just use fetch all
stmt = stmt.order_by(desc('growth'))
stmt = stmt.limit(5)

results = connection.execute(stmt).fetchall()
print("US Top 5 Population Growth by Age Group 2000-2008", '*'*30)
[print(x[0],x[1]) for x in results]

#Case Stamtements *********************************************************************
#Case statements are like logical operators
#they accept a list of conditions to match, and a column for placing values that match that condition
#the list of conditions SHOULD END IN AN ELSE clause that tells it what to do 
#if those conditions do not match
#these will demo the case statements, and it works differently than a WHERE clause
#even if you can get the same results sometimes

#an example is if we wanted the sum of 2008 population of New York
#for the sake of demonstration, we will use the case statement

#now this statement looks a little poluted, by I'll explain
stmt = select([ #classic select query
	func.sum( #you want the sum of something
		case([ #case, let it know you want to evaluate something before geting a value
			(census.columns.state == 'New York', #what to evaluate
			census.columns.pop2008) #what to do if true
		], else_=0))]) #what to do if not true

results = connection.execute(stmt).fetchall()
print('Population of New York 2008:',results[0][0],"*"*30)

#now let's try the total population over the age of 80 in 2008
stmt = select([func.sum(case([(census.columns.age>80, census.columns.pop2008)], else_=0))])
results = connection.execute(stmt).fetchall()
print('US Population of everyone over 80 in 2008:',results[0][0],"*"*30)

#Cast statement **********************************************************************
#now let's explore the cast statement
#you use the cast statement you change one data type to another
#this is useful for many reasons
#an example would be let's see what percent New York's population is compared to total US population
#this query will be kinda long
stmt = select([ #just begin the select query
	(func.sum( #sum stuff
		case([ #what you sum (which happens to be a case statement)
			(census.columns.state == 'New York', #condition
			census.columns.pop2008) #value if true
		], else_=0)) / #else=0, also I want to divide that sum by something
	cast(func.sum(census.columns.pop2008), #cast statement, to divide properly I'll need floats
		Float) * 100).label('ny_percent')]) #what data type to cast to, and I gave it a name

results = connection.execute(stmt).fetchall()
print('Percent of US population living in New York in 2008:',results,"*"*10)

#NOTE: what is returned isn't actually a 'float' data type. It's 'Decimal'
#which is generally a data type for a lossless way of storing rational numbers.
#so since this is SQLite which isn't a full fledged SQL DB at all, it may not support it fully

#to avoid building hard to read queries like that, you can break them up piece meal
#let's get the percent of the population under 18 in 2008
under_18 = func.sum(case([(census.columns.age<18, census.columns.pop2008)], else_=0))
pop_2008 = cast(func.sum(census.columns.pop2008), Float)
stmt = select([(under_18 / pop_2008 * 100).label('percent_under_18')])
results = connection.execute(stmt).fetchall()
print('Percent of US population under 18 in 2008:',results,"*"*19)

