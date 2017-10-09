#based on a course I got on PluralSight.com "Python - Beyond Basics"

#what we are doing is building a file reader
#we will start with a 'reader' object (class)
class Reader:
	#basically the __init__ method of a class is the constructor
	def __init__(self,filename):
		#self.ANYTHING is just the instance data, ie what class attributes will be
		self.filename = filename

		#so we will start the reader by opening some file
		#rt is the defualt which is 'reading' and 'text mode'
		self.f = open(self.filename, "rt")

	def close(self):
		#and we will add another method for closing the file, which for now
		#since it's literally just a file object (what open() returns) is we close it
		self.f.close()

	def read(self):
		#we also want to be able to read our file!
		#in which we will want to return something
		#using the .read() method will send all the characters untill EOF
		return self.f.read()



#here is it in terminal
'''
christian@christian-900X3L:~/PythonTutorials/Packages$ python3
Python 3.5.2 (default, Sep 14 2017, 22:51:06) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import reader.reader
reader is being imported! Rembmer to check this __init__.py for package set up help!
>>> reader.reader.__file__
'/home/christian/PythonTutorials/Packages/reader/reader.py'
'''
#now we get it to use it's functionality
'''
>>> r = reader.reader.Reader('reader/reader.py')
>>> r.read()
'#based on a course I got on PluralSight.com "Python - Beyond Basics"\n\n#what we are doing is building a file reader\n#we will start with a \'reader\' object (class)\nclass Reader:\n\t#basically the __init__ method of a class is the constructor\n\tdef __init__(self,filename):\n\t\t#self.ANYTHING is just the instance data, ie what class attributes will be\n\t\tself.filename = filename\n\n\t\t#so we will start the reader by opening some file\n\t\t#rt is the defualt which is \'reading\' and \'text mode\'\n\t\tself.f = open(self.filename, "rt")\n\n\tdef close(self):\n\t\t#and we will add another method for closing the file, which for now\n\t\t#since it\'s literally just a file object (what open() returns) is we close it\n\t\tself.f.close()\n\n\tdef read(self):\n\t\t#we also want to be able to read our file!\n\t\t#in which we will want to return something\n\t\t#using the .read() method will send all the characters untill EOF\n\t\treturn self.f.read()\n\n\n\n#here is it in terminal\n\'\'\'\nchristian@christian-900X3L:~/PythonTutorials/Packages$ python3\nPython 3.5.2 (default, Sep 14 2017, 22:51:06) \n[GCC 5.4.0 20160609] on linux\nType "help", "copyright", "credits" or "license" for more information.\n>>> import reader.reader\nreader is being imported! Rembmer to check this __init__.py for package set up help!\n>>> reader.reader.__file__\n\'/home/christian/PythonTutorials/Packages/reader/reader.py\'\n\'\'\'\n'
>>> r.close()
'''
#and this is after I elevated this Reader class to the top level reader package to make it easier to use
'''
christian@christian-900X3L:~/PythonTutorials/Packages$ python3
Python 3.5.2 (default, Sep 14 2017, 22:51:06) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import reader
reader is being imported! Rembmer to check this __init__.py for package set up help!
>>> r = reader.Reader('reader/__init__.py')
>>> r.read()
'#made based on a class I got on PluralSight.com "Python - Beyond Basics"\n\n#here is how I made this!\n\'\'\'\nchristian@christian-900X3L:~/PythonTutorials/Packages$ mkdir reader\nchristian@christian-900X3L:~/PythonTutorials/Packages$ touch reader/__init__.py\n\'\'\'\n#it is what let\'s python know it\'s a module!\n\'\'\'\nchristian@christian-900X3L:~/PythonTutorials/Packages$ python3\nPython 3.5.2 (default, Sep 14 2017, 22:51:06) \n[GCC 5.4.0 20160609] on linux\nType "help", "copyright", "credits" or "license" for more information.\n>>> import reader\n>>> type(reader)\n<class \'module\'>\n>>> reader.__file__\n\'/home/christian/PythonTutorials/Packages/reader/__init__.py\'\n\'\'\'\n#so we can see that \'reader\' is a module\n#and the the source file that is imported with reader is the package init file in the reader\n#directory, so in other words a python package is just a folder with a __init__.py file\n#and to prove it, I\'ve added some python code to this file to show it how it\'s imported\nprint(\'reader is being imported! Rembmer to check this __init__.py for package set up help!\')\n\'\'\'\n>>> import reader\nreader is being imported!\n\'\'\'\n\n#__init__.py files normally include nothing inside, but it\'s still normal for them to do things\n\n#also remember that everything in this file is run (just like __init__ of a class)\n#when the package is imported, so we will elevate the Reader() class up\nfrom reader.reader import Reader\n'
>>> r.close()
'''
