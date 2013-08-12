#!/usr/local/bin/python
#Project Euler 

# Largest prime factor
# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

from math import sqrt

def divandconquer(numin):
  factor = 2
  target = numin
  newtarget = target

  while factor <= numin:
    if factor > sqrt(newtarget):
      return newtarget

    if target % factor == 0:
        newtarget = target/factor
        target = newtarget

    else:
      factor += 1
	
print divandconquer(600851475143)

#print divandconquer(20)