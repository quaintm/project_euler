#!/usr/local/bin/python
#Project Euler 

# Smallest multiple
# Problem 5
# 2520 is the smallest number that can be divided by each of the numbers 
# from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by 
# all of the numbers from 1 to 20?

def factorsOf(numin):
  factlist = {}
  div =  2
  while div <= numin:
    if numin % div == 0:
      numin /= div
      if div in factlist:
        factlist[div] += 1
      else:
        factlist[div] = 1
    else:
      div += 1
  return factlist


def compFactors(upbound):
  allfactorsdict = {}
  for i in xrange(upbound,2,-1):
    itemfactors = factorsOf(i)
    for a in itemfactors:
      if a in allfactorsdict:
        if allfactorsdict[a] < itemfactors[a]:
          allfactorsdict[a] = itemfactors[a]
      else:
        allfactorsdict[a] = itemfactors[a]
  return allfactorsdict


def LCMult(upbound):
  multiple = 1

  factorlist = compFactors(upbound)
  for q in factorlist:
    multiple *= q**factorlist[q]
  return multiple


print LCMult(20)
