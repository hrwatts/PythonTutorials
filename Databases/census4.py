#census4.py
#based on a course I got from DataCamp.com "Introduction to Databases in Python"
#SQLite, SQLAlchemy+Pandas, plotting results

import pandas as pd
import matplotlib.pyplot as plt
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

#A pandas DataFrame can take a SQLAlchemy ResultSet as an argument
#but you will need to supply the column names separately
#let's take a query we did in census3.py
stmt = select([census.columns.sex, func.sum(census.columns.pop2008).label('pop2008_sum')])
stmt = stmt.group_by(census.columns.sex)
results = connection.execute(stmt).fetchall()

#now we just use the ResultSet as the argument for pandas.DataFrame()
df = pd.DataFrame(results)
print(df)

#NOTE: pandas won't automatically import the column names at this time, so you must do it manually
#usually with just the keys of the first result, that's the easiest way to ensure all columns are met
df.columns = results[0].keys()
print(df)

df.plot.bar()
plt.xticks(df.index,df.sex)
plt.show()
