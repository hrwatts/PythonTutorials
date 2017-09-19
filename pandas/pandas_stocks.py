#pandas_stocks.py
#demonstrate some powerful uses of the pandas library
#based on a course I got at DataCamp.com "pandas Foundations"

import numpy as np
import pandas as pd
from urllib.request import urlopen

#urlopen yeilds a generator, so I need 3
url = ('https://assets.datacamp.com/production/'+
    'course_1639/datasets/messy_stock_data.tsv')

raw_data = urlopen(url)
raw_data2 = urlopen(url)
raw_data3 = urlopen(url)

#so this data is a .tsv of text seperated values file
#but it is absolute garbage
#take a look (* is the splat operator for iterables)
print(*raw_data)

#so we want this valuble stock data from the internet
#we will use pandas to make this right
df = pd.read_csv(raw_data2)
print(df)

#it is so messy pandas won't read it well automatically
#let's use some of arguments to fix this
#we see this is not a 'c'sv but values seperated by a space
#use delimeter argument to denote this
#the 'header' or column labels are not on the 1st row, but the 3rd
#and there are comments in our .tsv marked with '#' don't include them
df = pd.read_csv(raw_data3, delimiter=' ', header=3, comment='#')
print(df)
