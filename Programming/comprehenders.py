#List Comprehenders
#python3 ~/Documents/pyfiles/pro/comprehenders.py
#made from a course I got at Datacamp.com 'Python Datascience Toolbox Part2'

#you use list comprehenders as a more efficient way to make list
#that would be done by for loop
#basically all you need is an iterator, iterator variable to represent each element,
#and an output, all in square brackets (because it's a list)
nums = [0,3,6,12,44]
nums_plus = [num+1 for num in nums]
print(nums_plus)

#you can nest list comprehenders too
#such as populating a matrix
matrix = [[col for col in range(0,5)] for row in range(0,5)]
for row in matrix:
	print(row)

#you can also filter out elements with conditionals
#this is the same building of a matrix, but this time only even numbers
even_matrix =[[col for col in range(0,5) if col%2==0] for row in range(0,5) if row%2==0]
for row in even_matrix:
	print(row)

#conditionals can even be done more advanced if-else
#similar matrix as the first, but if odd number place odd instead
new_even_matrix =[[col if col%2==0 else 'odd' for col in range(0,5)] for row in range(0,5)]
for row in new_even_matrix:
	print(row)

#you can also make dictionaries this way, basically the same way
neg_diction={num: -num for num in range(0,5)}
print(neg_diction)

#generators are also useful in the same way, except, they don't
#store the values in memory as a list, but instead it's a sequence you
#call to generate those values
#made with parenthesis
odd_num_gen = (num for num in range(0,10) if num%2==1)

#see, now it's just a generator object
print(odd_num_gen)

#but you can use it to make the values in the sequence
print(next(odd_num_gen))
print(list(odd_num_gen))

#generators can also be used specially with functions
#generator functions don't return stuff, they yield values
def odd_gen_fun(n):
	"""Generates Odd Values from 0 to N"""
	i=0
	while i<n:
		if i%2==1:
			yield i
		i= i+1

#now we will use it to make odd numbers
num_gen = odd_gen_fun(14)
print(*num_gen)

#output to console
'''
[1, 4, 7, 13, 45]
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4]
[0, 2, 4]
[0, 2, 4]
[0, 2, 4]
[0, 'odd', 2, 'odd', 4]
[0, 'odd', 2, 'odd', 4]
[0, 'odd', 2, 'odd', 4]
[0, 'odd', 2, 'odd', 4]
[0, 'odd', 2, 'odd', 4]
{0: 0, 1: -1, 2: -2, 3: -3, 4: -4}
<generator object <genexpr> at 0x7f8d38361ba0>
1
[3, 5, 7, 9]
1 3 5 7 9 11 13
'''
