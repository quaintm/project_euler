#!/usr/local/bin/python
#Project Euler 

# Largest palindrome product
# Problem 4
# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def ispalindrome(numin):
  pal = str(numin)

  for digit in range(int(len(pal)/2)):
    if pal[digit] != pal[len(pal)-digit-1]:
      return FALSE
  return TRUE

def findfirstpal():
  firstpal = 0
  for i in xrange(999,100,-1):
    for j in xrange(i,100,-1):
      if ispalindrome(i*j):
        firstpal = i*j
        return firstpal, i, j

def findmaxpal():
  area, x1, y1 = findfirstpal()

  for i in xrange(x1,y1,-1):
    for j in xrange(y1,x1):
      if ispalindrome(i*j):
        if i * j > area:
          area = i*j
          x1 = i
          y1 = j
  return area, x1, y1
          
print findfirstpal()
print findmaxpal()