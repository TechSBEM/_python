print("Q1...Write a function that computes the volume of a sphere given its radius.")
import math

def vol(rad):

    return (4/3)* math.pi * (rad**3)

print(vol(3))



print("\n\nQ2...Write a function that checks whether a number is in a given range (inclusive of high and low)")
# def run_check(num, low, high):
#     if not type(int):
#         return 0
#     for my_num in range(low, high+1):
#         if num == my_num:
#             return  True

def run_check(num, low, high):
    if not isinstance(num, int):
        return  0
    if low <= num <= high:
        return True
    else:
        return False

print(run_check(10,2,7))



import _collections
print("\n\nQ3....Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.")
def check_upper(a):
    pass

def up_lower(s):
    no_space= s.replace(" ","")
    count_upper= 0
    count_lower= 0
    for char in no_space:
        #Checking whether it is an uppercase
        if char.isupper():
            count_upper +=1
        elif char.islower():
            count_lower +=1

    print(f"No. of Upper case characters : {count_upper}")
    print(f"No. of Lower case Characters: {count_lower}")
    return True

print(up_lower("Hello Mr. Rogers, how are you this fine Tuesday?"))

print("\n\nQ4...Write a Python function that takes a list and returns a new list with unique elements of the first list")
def unique_list(lst):
    return list(set(lst))

print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))




print("\n\nQ4...Write a Python function to multiply all the numbers in a list.")
def multiply(lis):
    mu = math.prod(lis, start=1)
    return mu

def multiply_with_loops(lis):
    times= 1
    for num in lis:
        times=times *num
    return times


print(math.prod([1,2,3,4],  start=1))
print(multiply([1,2,3,-4]))
print(multiply_with_loops([1,2,3,-4]))



print('Q5...Write a Python function that checks whether a word or phrase is palindrome or not.')
def palindrome(s):
    check = [x for x in str(s) [::-1]]
    print(list(s))

    if check == list(s):
        print(str(check))
        return True
    else:
        return False


print(palindrome("hehheh"))