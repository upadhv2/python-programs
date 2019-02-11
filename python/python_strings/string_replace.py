'''
>>> str = "vishal upadhye"
>>> print str.replace("vishal", "Avani")
Avani upadhye
>>> 
>>> 
>>> print str.replace("Ava", "prii")
vishal upadhye
>>> print str.replace("Ava", "pri")
vishal upadhye
>>> print str.replace("v", "p", 1)
pishal upadhye
>>> print str.replace("a", "p", 1)
vishpl upadhye
>>> print str.replace("a", "p", 2)
vishpl uppdhye
>>> print str.replace("a", "p", 100)
vishpl uppdhye
>>> print str.replace("a", "p", len(str))
vishpl uppdhye
>>> print str.replace("a", "", len(str))
vishl updhye
>>> 
>>> 
>>> 
>>> print str.replace("a", ".", len(str))
vish.l up.dhye
>>> 
'''

str = "aaaaaaaaaaaavvvvvvvvvvvvvaaaaaaaa"
print str.replace("a", ".", len(str))
