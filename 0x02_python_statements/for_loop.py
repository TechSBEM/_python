print('\n\n ---------------------For lop-----------------')
# For loop in list
myList = [1,2,3,4,5,6,7,8,9,10]
sumUpList = 0
for num in myList:
    # Check even and olde
    if num %2 ==0:
        print(f'Even: {num}')
    else:
        print(f'Odd:  {num}')
    sumUpList += num

print(f'The sum of all the numbers in the list is: {sumUpList}')

print('\n\n---------Tuples Unpacking with for Loop------------')
myTupleList = [(1,2), (3,4), (4, 5), (5, 6), (6,7)]

print(f"number of items in the list is: {len(myTupleList)}")

for (a, b) in myTupleList:
    print(a)
    print(b)



print('-----------Iterating Dictiomary with for loop----------')
# By default, you will get the keys when iterating the Dictionary
myDict = {'k1 ':1, 'k2': 'Kofi', "k3": True}

for (key, value) in myDict.items():
    # print only my values
    print(value)