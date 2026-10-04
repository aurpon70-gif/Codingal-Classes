#Create a tuple with different data types
tuplex = ("tuple", False, 3.2, 1)
print(tuplex)

#Create a tuple
tuplex = (4, 6, 2, 8, 3, 1)
print(tuplex)
#Tuples are immutable, so you can't change their elements directly.
#Using merge or concatenation to create a new tuple instead
tuplex = tuplex + (9,)
print(tuplex)

#Counts the number of occurences of item 50 from a tuple
tuple1 = (50, 10, 60, 70, 50)

print(tuple1.count(50))

#Crreate a tuple
tuplex = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)

_slice = tuplex[3:5]
print(_slice)
_slice = tuplex[:6]
print(_slice)
