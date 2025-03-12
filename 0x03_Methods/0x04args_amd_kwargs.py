#*args(Non-keyword Arguments)
# Can take any number of arguments
print("-------------------*args------------------")
def myfunc(*args):
    return sum(args)

print(f' The sum of the 2,3,4,5,1,2,4,1,2  is: {myfunc(2,3,4,5,1,2,4,1,2)}')

print("\n\n----------------**kwargs-------------")
def myKwargs_funtion(**kwargs):
    for key, values in kwargs.items():
        if key== 'fruit':
            print(f'My favorite fruit is {values}')
        else:
            print('No fruit found')


myKwargs_funtion(car='Bugatti', fruit ='Orange', drink='water')



print("-----------------Using both-------------")
def myfunc(*args, **kwargs):
    print(args)
    print(kwargs)
    print(f'I want {args[0]} number of {kwargs['fruits']}')

myfunc(10,20,30, food='fufu', fruits='mango')