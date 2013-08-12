#!/usr/local/bin/python
#Project Euler 

# Sum square difference
# Problem 6
# The sum of the squares of the first ten natural numbers is,

# 1**2 + 2**2 + ... + 10**2 = 385
# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the 
# first ten natural numbers and the square of the sum 
# is 3025  385 = 2640.

# Find the difference between the sum of the squares of the 
# first one hundred natural numbers and the square of the sum.

def sumOfSquare(upbound):
  sum1 = 0
  for a in xrange(1,upbound+1):
    sum1 += a**2
  return sum1

#print sumOfSquare(100)

def squareOfSum(upbound):
  sum2 = 0
  for a in xrange(1,upbound+1):
    sum2 += a
  return sum2**2

#print squareOfSum(100)

print squareOfSum(100) - sumOfSquare(100)