#made based on a class I got on PluralSight.com "Python - Beyond Basics"

#here is how I made this!
'''
christian@christian-900X3L:~/PythonTutorials/Packages$ mkdir reader
christian@christian-900X3L:~/PythonTutorials/Packages$ touch reader/__init__.py
'''
#it is what let's python know it's a module!
'''
christian@christian-900X3L:~/PythonTutorials/Packages$ python3
Python 3.5.2 (default, Sep 14 2017, 22:51:06) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import reader
>>> type(reader)
<class 'module'>
>>> reader.__file__
'/home/christian/PythonTutorials/Packages/reader/__init__.py'
'''
#so we can see that 'reader' is a module
#and the the source file that is imported with reader is the package init file in the reader
#directory, so in other words a python package is just a folder with a __init__.py file
#and to prove it, I've added some python code to this file to show it how it's imported
print('reader is being imported! Rembmer to check this __init__.py for package set up help!')
'''
>>> import reader
reader is being imported!
'''

#__init__.py files normally include nothing inside, but it's still normal for them to do things

#also remember that everything in this file is run (just like __init__ of a class)
#when the package is imported, so we will elevate the Reader() class up
from reader.reader import Reader
from reader.reader2 import Reader2
