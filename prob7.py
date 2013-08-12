#!/usr/local/bin/python
#Project Euler 

# 10001st prime
# Problem 7
# By arraying the first six prime numbers: 
# 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

def findPrimes(tempbound):
  primearray = range(2,tempbound+1)

  for j in primearray:
    n = 2
    jarray = ()
    while j*n <= tempbound:
      jarray += (j*n,)
      n += 1

    primearray = set(primearray) - set(jarray)       
  primearray = tuple(primearray)
  return primearray

print findPrimes(11)
#print findPrimes(100)

def primearray(nthprime):
  arrayOfPrimes = ()
  tempbound = 1
  while len(arrayOfPrimes) <= nthprime+1:
    tempbound += 10
    arrayOfPrimes += findPrimes(tempbound)
    #print "number of primes found: %d" % len(arrayOfPrimes)
    print arrayOfPrimes

  return "%dth prime: %d" % (nthprime, arrayOfPrimes[nthprime])

print primearray(11)