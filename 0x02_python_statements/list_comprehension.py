#----------------Comprehension-------------
#Make you write concise and structed code
# Syntax:   new_list = [expression for item in iterable if condition]

# List---Comprehension
mylist = []

for num in 'Words On':
 mylist.append(num)

print(mylist)

print('\n\n--------Use List Comprehension for the same result-----------')

myComprehendedList =[char for char in 'Words On']
print(myComprehendedList)


print('\n\n------List Comprehension to find even numbers--------')
myEvenListComprehension= [num for num in range(20) if num%2 ==0]
print(myEvenListComprehension)