def hello ():
    print('hello')
    print('hi')

def your_name(name):
    print(f'Hello {name}')

# your_name("Emma")

# When a function is returned with a value, it can be stored
def func_name(name):
    return f'My name is {name}'

my_name= func_name("Emma")
print(my_name)