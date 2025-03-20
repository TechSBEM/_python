#Linear search

def  linear_search(list, target):
     """
     Returns the index position of the target if found, else returns None
     The length of the function is a constant time
     """
     count =0
     for x in range(len(list)):
         if list[x]== target:
             print(f'Number of time it iterated to get the target: {count}')
             return x
         count +=1
     return None



def verify(index_value):
    """
    print not None: Print Index Position
    Print: Target not found in list ----> for None
    """
    if index_value is not None:
        print('Target found at index: ', index_value)
    else:
        print('Target not found in list')

numbers = [x for x in range(1,101)]
results = linear_search(numbers, 45)
print(results)
verify(results)