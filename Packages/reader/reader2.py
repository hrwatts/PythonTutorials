#based on a course I got on PluralSight.com "Python - Beyond Basics"
#building off of what reader.py does, mostly working with the compressed subpackages

import os
from reader.compressed import bzipped, gzipped

#just a dictionary for associating file extentions to our compressed readers
extention_map = {
	'.bz2': bzipped.opener,
	'.gz': gzipped.opener,
}

class Reader2:
	def __init__(self,filename):
		#os.path.splitext splits the extention off a filename into a list, [1] is the ext
		extention = os.path.splitext(filename)[1]
		#so opener is either going to be 1) the value of a key found in extention_map
		#or 2) the open() function
		#it should be noted both of these are functions though
		opener = extention_map.get(extention, open)
		self.f = opener(filename, "rt")

	def close(self):
		self.f.close()

	def read(self):
		return self.f.read()

#now we are ready to run this in the REPL
'''
>>> import reader
reader is being imported! Rembmer to check this __init__.py for package set up help!
>>> r = reader.Reader2('test.bz2')
>>> r.read()
'data compressed with bz2'
>>> r_gz = reader.Reader2('test.gz')
>>> r_gz.read()
'data compressed with gz'
'''
