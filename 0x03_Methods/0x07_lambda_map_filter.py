#map() funtion
#Syntax: map(function, iterable) -->map object
#Pass the function as an argument don't add a parathesis
print("------------------------map()--------------------------")

def square(x):
    return x**2
my_nums = [1,2,3,4,5]
do = list(map(square, my_nums))
print(do)

def splice(mystring):
    if len(mystring)%2== 0:
        return 'Even'
    else:
        return mystring[0]

splice_check= list(map(splice, ['Andy', "Eve",'You' ]))
print(splice_check)



print("---------------filter()----------------------")
# Return iterators that returns True or False based on the function given
def check_even(num):
    return num%2==0

my_filter=list(filter(check_even, [1,2,3,4,5,6]))

print(my_filter)


print("----------------lambda Expression----------------")

squared =lambda x: x**2
print(squared(4))

even = list(map(lambda x: x%2==0, [1,2,3,4,5,6,7,8,9]))
print(even)

even = list(filter(lambda x: x%2==0, [1,2,3,4,5,6,7,8,9]))
print(even)

#Getting the first letters of a string
get_first_letter=list(map(lambda x: x[0], ['Andy','Eve', 'Sally']))
print(get_first_letter)

