#!/usr/bin/env python
# coding: utf-8

# In[11]:


#Part I - Implement the Fibonnaci Sequence

def fibonnaci(n):
    #Return the nth Fibonacci number using recursion
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonnaci(n - 1) + fibonnaci(n - 2)

#Driver code
print(fibonnaci(3))


# In[17]:


#Part II - Implement Euclid’s GCD Algorithm

def gcd(a,b):
    #Return the greatest common divisor of a and b using recursion
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

#Driver code    
print(gcd(10,100))


# In[20]:


#Part III - String Comparison

def compareTo(s1, s2):
    #Compare two strings recursively
    
    if len(s1) == 0 and len(s2) == 0: #When both strings are equal
        return 0
    if len(s1) == 0: #When the first string is smaller
        return -1
    if len(s2) == 0: #When the first string is bigger
        return 1
    if s1[0] != s2[0]:
        return ord(s1[0]) - ord(s2[0])
    else:
        return compareTo(s1[1:], s2[1:])
    
print(compareTo('afegf','afeeegf'))

