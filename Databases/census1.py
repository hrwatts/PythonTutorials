#census1.py
#based on a course I got from DataCamp.com "Introduction to Databases in Python"
#SQLAlchemy, SQLite, reflection objects

from sqlalchemy import create_engine, Table, MetaData, select

#so unlike connecting to an actual DB, like your local host, reading SQLite files
#is really just opening up a file, no username or password needed when making the engine
#so all you need is the "dialect" and filepath

#census.sqlite is just some really basic info about US state populations
engine = create_engine("sqlite:///census.sqlite")

#show that it is working
connection = engine.connect()
print(engine.table_names())

#you aren't just instantiating is here just for ease of not retyping it
#you are building the metadata for the ENTIRE schema
#every time you use this in table, it builds into MetaData
metadata = MetaData()

#now let's make a relected table out of the census table
census = Table('census', metadata, autoload=True, autoload_with=engine)

#now that it is in memory, let's use it
#print the metadata of the census table
print(repr(census))

#to show what I meant about metadata being built along with tables
#I'll show that metadata has the metadata of census in it too
print(repr(census) == repr(metadata.tables['census']))

#it is the same!

#so notice all the objects inside of this Table
#let us just target to columns to be printed out
print("\nColumns in Census Table:", ", ".join(census.columns.keys()))

#now obviously these next few things are just basic SQL commands, nothing too fancy
#also, these just send raw SQL commands, no guard for SQL injection
#it's just for demonstration
stmt = "select state from census"

#much like any other SQL connector, it isn't just going to give you some text result of your
#query, the result could be complicated, so you store the result of a query to a ResultProxy
result_proxy = connection.execute(stmt)

print("The type of an execution result is:",type(result_proxy))

#if you want the data the query actually found (as a list) use the .fetchall()
#when you use a fetch method on a ResultProxy you get what is called a result set
#obvious .fetchall() returns a list, but from working with other sql connectors
#you understand. Anyways this allows us to more precisely control the data we pull using a query
results = result_proxy.fetchall()

#take a look
print("Size of Results:",len(results),"Type of Results",type(results),"\nFirst 5 values:")
[print(x) for x in results[:5]]

#so each position in the result set is a row that was returned as a result of the query
#right now, we asked for just one thing so it's not very interesting, so let's change it
result_proxy = connection.execute("select * from census where state=\'Georgia\'")
results = result_proxy.fetchall()

#just take a look at this first row, very different
print("First row from Georgia query:",results[0])

#also of note is that this is a RowProxy() object within a list of RowProxy's
#also it could be made into a DataFrame later
print("Type of a row from a result set:",type(results[0]))

#being a RowProxy instead of just raw data, it retains useful information, such as the column names
print("Column names from RowProxy:",results[0].keys())

#also, a RowProxy allows indexing by position and column names, both using brackets []
#such as ['state'] or [0]


#you really don't want to write our SQL queries as a string and execute them
#it is more difficult (to less advanced SQL users), long, and confusing
#there is a better way! In the MySQL connector they are called prepared statements
#SQLAlchemy does you one better, it builds you a string using functions
#let's do "select * from census" this way
stmt = select([census])
print("The SQLAlchemy Select:",stmt)

#you can imagine the reason for using list as the arguments
#given what functionality it is suppose to reflect for ANY select query

#more advanced features, like better SQLAlchemy queries and moving over to pandas to come later

