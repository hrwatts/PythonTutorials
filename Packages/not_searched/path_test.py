#based on a class I got on PluralSight.com "Python - Beyond Basics"
#working with python paths


def found ():
	print('Python found me!')

#if you want to run this as a module in python (by importing it) you'll need to
#add it to python's search path
#just running import path_test won't work
'''
>>> import path_test
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named 'path_test'
'''
#add it to the path a number of ways
#1) appending it
'''
>>> import sys
>>> sys.path
['', '/opt/ros/lunar/lib/python2.7/dist-packages', '/usr/lib/python35.zip', '/usr/lib/python3.5', '/usr/lib/python3.5/plat-x86_64-linux-gnu', '/usr/lib/python3.5/lib-dynload', '/usr/local/lib/python3.5/dist-packages', '/usr/local/lib/python3.5/dist-packages/ungsc2-0.2-py3.5.egg', '/usr/lib/python3/dist-packages']
>>> sys.path.append('not_searched')
>>> import path_test
>>> path_test.found()
Python found me!
>>> 
'''
#but this only adds the directory for the current python session
#or a much safer (and permenant way)
#2) is by adding the directory to the PYTHONPATH environment variable on your computer
#it follows the same PATH sintax as the rest of your computer, this is on Linux so :
'''
christian@christian-900X3L:~/PythonTutorials/Packages$ printenv PYTHONPATH
/opt/ros/lunar/lib/python2.7/dist-packages

christian@christian-900X3L:~/PythonTutorials/Packages$ export PYTHONPATH=not_searched

christian@christian-900X3L:~/PythonTutorials/Packages$ printenv PYTHONPATH
not_searched

christian@christian-900X3L:~/PythonTutorials/Packages$ python3
Python 3.5.2 (default, Sep 14 2017, 22:51:06) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> sys.path
['', '/home/christian/PythonTutorials/Packages/not_searched', '/usr/lib/python35.zip', '/usr/lib/python3.5', '/usr/lib/python3.5/plat-x86_64-linux-gnu', '/usr/lib/python3.5/lib-dynload', '/usr/local/lib/python3.5/dist-packages', '/usr/local/lib/python3.5/dist-packages/ungsc2-0.2-py3.5.egg', '/usr/lib/python3/dist-packages']
>>> import path_test
>>> path_test.found()
Python found me!
'''
