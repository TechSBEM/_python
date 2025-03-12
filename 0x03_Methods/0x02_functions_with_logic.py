def check_even_list(num_list):
    # return all the even number in a list
    even=[]
    for num in num_list:
        if num %2==0:
            even.append(num)
            return True
        else:
            # return False: We didn't not return false because it will always do so with one non-even number
            pass

    print(even)
    return False

check_even_list([1,2,3,4,5,8])
result= check_even_list([1,2,3,4,5,8])
print(result)


def check_even_list(num_list):
    # return all the even number in a list
    even_list=[]
    for num in num_list:
        if num %2==0:
            even_list.append(num)

        else:
            # return False: We didn't not return false because it will always do so with one non-even number
            pass
    return even_list

result= check_even_list([1,2,3,4,5,8])
print(result)