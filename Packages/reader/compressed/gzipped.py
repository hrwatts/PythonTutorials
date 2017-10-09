#a file reader for opening compressed files
#based on a course I got from PluralSight.com 'Python Beyond Basics'

import gzip
import sys

#create an instance of the gzip.open function
opener = gzip.open

if __name__ == '__main__':
	#argv are argument values that you put in at command line
	#w is 'write' access, and also allows you to create files that aren't currently there
	f = gzip.open(sys.argv[1], mode='wt')
	f.write(' '.join(sys.argv[2:]))
	f.close()

#now let's try it out!
'''
>>> import reader.compressed
>>> import reader.compressed.gzipped
>>> import reader.compressed.bzipped
'''
#no errors so it works great!
#now let's make a file with this
#note how argv plays into this
'''
christian@christian-900X3L:~/PythonTutorials/Packages$ python3 -m reader.compressed.gzipped test.gz data compressed with gz
'''
#take a look at what we have now
'''
christian@christian-900X3L:~/PythonTutorials/Packages$ ls
not_searched  reader  test.bz2  test.gz
'''
