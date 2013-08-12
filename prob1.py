#!/usr/local/bin/python
#Project Euler 
# Multiples of 3 and 5
# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000

def numcheck(num1):
	if float(num1)/float(3) == int(num1)/int(3):
		return num1

	elif float(num1)/float(5) == int(num1)/int(5):
		return num1

	else:
		return 0

def sumofchecks(upbound):
	multisum = 0
	for x in range(0,upbound):
		multisum += numcheck(x)

	return multisum

print sumofchecks(1000)
