#Finding the 'Employee of the month" based on the number of hours worked.
# We will be using "tuple"
import random

employees = (('Steven', 100), ('Mr Asare', 90), ('Promise', 130), ('Orterga', 495))

def check_employee(employee_list):
    employee_name = ''
    employee_hours = 0

    for (name, hours) in employee_list:
        # employee_hours =
        print(hours)
        # print(name)

        if  employee_hours <= hours:
            employee_hours =hours
            employee_name =name

    return employee_name, employee_hours


results = check_employee(employees)
# Performing tuple unpacking with functions
name,time =check_employee(employees)
print(results)
print(f'The employee who won is {name} with {time} hrs')

mylist =[1,2,4,3,5,2,4]


# Get the list
# Shuffle the list in a variable
# return the variable

def func_shuffle(mylist):
    random.shuffle(mylist)
    return mylist


all= func_shuffle(mylist)
print(all)