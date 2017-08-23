#to show off iterators and their uses
#1984 Congressional Voting database
#python3 ~/Documents/pyfiles/pro/iterators.py
#made from a course I got at Datacamp.com 'Python Datascience Toolbox Part2'

#imports
import pandas as pd
from urllib.request import urlopen

#download the database from the internet
raw_data = urlopen('https://archive.ics.uci.edu/ml/machine-learning-databases/voting-records/house-votes-84.data')

#one important use of iterators is that they can be used to read in huge amounts of data in chunks
#obviously this data doesn't qualify but you can imagine
#this is how you can use pandas to iterate over it
#let's say you wanted to know the number of democrats in congress
democrat=[]
num_dems=0

for chunk in pd.read_csv(raw_data, header=None, chunksize=10):
	#obviously 10 is really small but this is for demo purposes!
	democrat.append(sum(chunk[0]=='democrat'))
	#obviously we also can just sum them up on the spot.
	num_dems+=sum(chunk[0]=='democrat')

#now we just take a peal at what it contains
print(democrat)

#now that we have performed the desired operation on each chunk,
#and stored its result, we can perform operations on the results
#this allows us to free up memory that might be wasted on data we don't
#need anymore
print('Number of Democrats in Congress: '+str(sum(democrat)))
print('Number of Democrats in Congress(2): '+str(num_dems))

#since the urlopen object is itself an iterator you can't exactly re-use it
#once you've iterated over it, so I'll make it again
raw_data2 = urlopen('https://archive.ics.uci.edu/ml/machine-learning-databases/voting-records/house-votes-84.data')
df = pd.read_csv(raw_data2, header=None)
print(df.head())

#let's do some more iterators
party=list(df.iloc[:,0])
print("Party: "+str(party[:4]))
handicap=list(df.iloc[:,1])
print('Handicap: '+str(handicap[:4]))

#zip up these lists, into a zip object which is an iterator
#of tuples that consist of matching indexed pairs of elements from what is zipped
votes=zip(party[:4], handicap[:4])

#using the splatter operator we can tell it to do it all at once
print("Party and Vote:")
print(*votes)

#output to console
'''
[6, 5, 9, 4, 9, 3, 6, 7, 4, 9, 8, 6, 4, 5, 5, 5, 7, 8, 9, 6, 7, 7, 5, 5, 6, 5, 8, 4, 7, 8, 3, 6, 8, 7, 4, 4, 7, 6, 10, 7, 3, 6, 8, 1]
Number of Democrats in Congress: 267
Number of Democrats in Congress(2): 267
           0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16
0  republican  n  y  n  y  y  y  n  n  n  y  ?  y  y  y  n  y
1  republican  n  y  n  y  y  y  n  n  n  n  n  y  y  y  n  ?
2    democrat  ?  y  y  ?  y  y  n  n  n  n  y  n  y  y  n  n
3    democrat  n  y  y  n  ?  y  n  n  n  n  y  n  y  n  n  y
4    democrat  y  y  y  n  y  y  n  n  n  n  y  ?  y  y  y  y
Party: ['republican', 'republican', 'democrat', 'democrat']
Handicap: ['n', 'n', '?', 'n']
Party and Vote:
('republican', 'n') ('republican', 'n') ('democrat', '?') ('democrat', 'n')
'''
