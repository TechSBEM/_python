# String concatenation
x= 'hi '
print( x + " you there")

# Concatenation multiplication
print( x *5)

print(x.upper())

# Print Formating
print('The {t} {t} {t}'.format('fox', t='tail', q='cares'))
print('---------------DICTIONARY-----------------')

#-------------- Dictionary
# Keys use strings
# Creating a dictionary
myDictionary = {'k1': 'car','my' : 23, 'k3': 'Bibsle', 'myArray': [2,3,4,5]}
print(myDictionary)

# Retrieving a value from a dictionary
print(myDictionary['my'])
# Adding value to a dictionay
myDictionary['bool']=True

print(myDictionary)


print('---------------tuple-------------')
# ---------------------Tuple
# In typles, there can be "slicing' and 'indexing'
# got some method: count() , index()
# Tuples are immutable

myTuple = (12,"Cars", [1,3,4,5], 12)
print(myTuple)
print(myTuple[2])
print(f' counting the number of times :12 appeared in the tuple=== { myTuple.count(12)}')



print('-----------------------------SET----------------------')
# --------------------------------SET
# got unique vaalues
# has methods like add()
# they are not ordered

mySet= set()
mySet.add(2)
mySet.add(3)

myList= [1,2,3,4,2,2,3,1,4,1,3,4]
print(mySet)
print(myList)
# Casting list into set
print(set(myList))
