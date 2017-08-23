#writing function basics
#python3 ~/Documents/pyfiles/pro/functions.py
#made from a course I got at Datacamp.com 'Python Datascience Toolbox Part1'

def sum_str(*vec, cap=False):
	'''sum_str() takes any lists of strings, and adds up the ASCII values of each character'''
	#that's how you write the docstring, which will display during help()

	suum=0
	
	#try-except, basic exception handling
	#if an exception occurs during code in try block, except block will run
	try:	
		#for loop
		for item in vec:
			#control flow (if, elif, else)
			if type(vec)==tuple:
				#if more than one arg is used in vec, it will be a tuple
				#(though, at this point a list/string)
				for word in item:
					if cap:
						word = word.upper()
					if len(word)>1:
						for char in word:
							suum=suum+ord(char)
					else:
						suum=suum+ord(word)
			elif type(vec)==list:
				if cap:
					item = item.upper()
				for char in item:
					suum=suum+ord(char)
			else:
				if cap:
					item = item.upper()
				suum=suum+ord(item)
	except:
		#explicitly raises an error of whatever kind I want
		raise TypeError('Must be a string, or a standard collection of strings')
	return suum

def key_print(**keys):
	out=[]
	for key,item in keys.items():
		out.append(str(key)+':'+str(item))
	return out
print(sum_str.__doc__)
print(sum_str(['apple','banana'], ['tomato', 'carrot'], 'apple', 'panda', cap=True))
print(sum_str(['apple','banana'], ['tomato', 'carrot']))
print(key_print(fname='Sam', lname='Smith'))
print(sum_str(4))

#output to console
'''
sum_str() takes any lists of strings, and adds up the ASCII values of each character
2440
2450
['lname:Smith', 'fname:Sam']
Traceback (most recent call last):
  File "/home/christian/Documents/pyfiles/pro/functions.py", line 20, in sum_str
    for word in item:
TypeError: 'int' object is not iterable

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/christian/Documents/pyfiles/pro/functions.py", line 51, in <module>
    print(sum_str(4))
  File "/home/christian/Documents/pyfiles/pro/functions.py", line 39, in sum_str
    raise TypeError('Must be a string, or a standard collection of strings')
TypeError: Must be a string, or a standard collection of strings
'''
