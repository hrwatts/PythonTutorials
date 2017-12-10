#census2.py
#based on a course I got from DataCamp.com "Introduction to Databases in Python"
#SQLAlchemy, Select Statements, Conjunctions, Ordering

from sqlalchemy import create_engine, Table, MetaData, select, or_, and_, not_

#practicing more advanced select queries using a census database and SQLAlchemy
engine = create_engine("sqlite:///census.sqlite")
connection = engine.connect()

#instantiate the metadata for this schema
metadata = MetaData()

#make reflected table
census = Table('census', metadata, autoload=True, autoload_with=engine)

#using SQLAlchemy's pythonic way of interacting with the database

#so it is select(FROM) you put a list of what tables to select from
stmt = select([census])

#now we can build on this query, without having to write it all at once
#use can use other comparison operators as you'd expect == <= >= !=
#but you can also use SQL specific operators in_(), like(), between(), and more
#which are available as methods on our columns objects
#check SQLAlchemy Docs for more
stmt = stmt.where(census.columns.state == 'California')

#the most interesting thing about this is it writes just like pandas and other python packages
#but it hasn't actually done any work yet! This statement hasn't been executed

#so we are going straight to the result set by using .fetchall() on the ResultProxy
results = connection.execute(stmt).fetchall()

#now let's see all the results of this query
print('California ' + "*"*70)
[print(x) for x in results]

#we will do some more advanced select queries
#all the states that start with 'New'
stmt = select([census])

#and just like above, you use the advanced operators as methods
stmt = stmt.where(census.columns.state.startswith('New'))

#A ResultProxy doesn't have to have a .fetch() method used on it to get the results
#It is also an interable that you can loop over
print('New States ' + "*"*70)
[print(result) for result in connection.execute(stmt)]

#you can use standard SQL conjunctions this way too
#such as and_(), not_(), or_()
#you can use them in a number of different ways
#we will use them here as a single argument to pass to the where clause
stmt = select([census])
stmt = stmt.where(
	or_(
	census.columns.state == 'Texas',
	census.columns.state == 'Georgia'
	)
)

print('Texas OR Georgia ' + "*"*70)
[print(result) for result in connection.execute(stmt)]

#the difference here is of course pulling the data and then filtering it
#or just calling the data you need
#it is always better to call just the data you need
#databases can get REALLY big

#AND conjunction
stmt = select([census]) #you don't really need this just because the privious one is Texas and Georgia
stmt = stmt.where(
	and_(
	census.columns.state == 'Georgia',
	census.columns.age == 22
	)
)
print('Georgia AND 22 ' + "*"*70)
[print(result) for result in connection.execute(stmt)]

#NOT clause
stmt = select([census])
stmt = stmt.where(
	and_(
	census.columns.state.startswith('New'),
	census.columns.sex == 'F',
	not_(census.columns.age < 80)
	)
)

print('New States AND women AND NOT younger than 80 ' + "*"*50)
[print(result) for result in connection.execute(stmt)]

#additionally we can blend some of our python skills into this
#like getting all the states from a list using the in_() method
states = ['Georgia','Florida','Alaska']
stmt = select([census])
stmt = stmt.where(
	and_(
	census.columns.state.in_(states),
	census.columns.age == 22
	)
)

print('States in list of states AND 22 years old ' + "*"*50)
[print(result) for result in connection.execute(stmt)]

#but it looks like Alaska is coming in right in the middle of Georgia!
#we can fix this by ordering the data, lets try alphabetically
stmt = select([census])
stmt = stmt.order_by(census.columns.state)
stmt = stmt.where(
	and_(
	census.columns.state.in_(states),
	census.columns.age == 22
	)
)
print('States in list of states AND 22 years old in order ' + "*"*41)
[print(result) for result in connection.execute(stmt)]

#NOTE: we don't need to build another query to do this
#if we are just fixing the last query, we could have just tagged it on to the end

#we can even sort by multiple columns
#just add multiple arguments to order_by, and it will order them in the order specified
#such as state and then population in 2000
stmt = select([census])
stmt = stmt.order_by(census.columns.state, census.columns.pop2000)
stmt = stmt.where(
	and_(
	census.columns.state.in_(states),
	census.columns.sex == 'M',
	census.columns.age.between(18,25)
	)
)
print('States from list AND male AND between 18-25 ordered by state and population in 2000 ' + "*"*8)
[print(result) for result in connection.execute(stmt)]
