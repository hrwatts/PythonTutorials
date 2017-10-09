#based on a course I got from PluralSight.com "Python Beyond Basics"
#working with bz2 files, and demoing subpackages

import bz2
import sys

opener = bz2.open

if __name__ == '__main__':
	#argv are argument values that you put in at command line
	#w is 'write' access, and also allows you to create files that aren't currently there
	f = bz2.open(sys.argv[1], mode='wt')
	f.write(' '.join(sys.argv[2:]))
	f.close()

#now let's try it out!
'''
>>> import reader.compressed
>>> import reader.compressed.gzipped
>>> import reader.compressed.bzipped
'''
#no errors so it works great!
#now lets make a file with this
#note how argv plays into this
'''
christian@christian-900X3L:~/PythonTutorials/Packages$ python3 -m reader.compressed.bzipped test.bz2 data compressed with bz2
'''
#take a look at our workspace
'''
christian@christian-900X3L:~/PythonTutorials/Packages$ ls
not_searched  reader  test.bz2  test.gz
'''
