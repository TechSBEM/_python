#----------------------range()----------------------
# Use in loop for iterating numbers
#Syntax = range(start, stop, step)
#The exact number at stop is exlusing witha default on 1 as it step
import random

print('------------rang()-------------')
all = ' '
for num in range(10):
    all =  all +str(num) +','
print(all)

for num in range(2, 11, 3):
    print(num)


#--------------------------enumerate----------------------
#Print the iterable whiles keeping track of it index
# returns (index, value)
print('-----------------enumerate()-----------------')
mylist= ['fire', 'water', 'earth', 'wind', 'all four nations']
for num in enumerate(mylist):
    # This will retain a tuple: Use tuple unpacking
    print(num)

print('---use tuple unpacking to achieve the same results above')
for (index, value) in enumerate(mylist):
    print(f"Index {index} has a value of: {value} ")

#zip()
#Zip is used to combined mutltiplel iterable
print('--------------------zip()----------------')
ageIterable= [10, 13,44, 29, 120]
namesIterable =('Kwame', "kofi", 'Yaa', 'Abena', "Akua")
zippedIterate = zip(namesIterable, ageIterable)

for name, age in zippedIterate:
    print(f'{name} is {age} years old')

print('\n\n-------------importing from a library------------')


from random import randint
random_number = randint(0, 99)
print(f'A random number form 0-99: {random_number}')