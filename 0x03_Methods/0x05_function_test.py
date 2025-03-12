#-----------Warm Up----------
#LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
print('------------Warm Up--------------')
def lesser_of_two_function(a,b):
    #both even
    if a% 2==0 and b%2 ==0:
    #**return the lesser
        return min(a,b)
    else:
        return max(a,b)
    #one or both odd,
    #** return the greater


check = lesser_of_two_function(2,5)
print(check)


#ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
def animal_crakers(words ):
    myword= []
    #Check first char
    for word in words.split():
        myword.append(word)

    if myword[0][0]==myword[1][0]:
    #Same: return True
        return True
    else:
    #Not same: return False
        return False

check= animal_crakers('Levelheaded Llama')
print(check)
check2 =animal_crakers('Crazy Kangaroo')
print(check2)




#MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
def makes_twenty(n1,n2):
    if (n1+n2)==20 or n1==20 or n2==20:
        return True
    else:
        return False

check = makes_twenty(20,10)
print(check)
check = makes_twenty(12,8)
print(check)
check = makes_twenty(2,3)
print(check)



print('\n\n\n------------level 1-------------')
#--------------------level 1---------------------------------

# Q1.....OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
def old_macdonalt(sent):
    new_name=''
    for num in range(len(sent)):
        if num==0 or num ==3 :
            new_name += sent[num].upper()
        else:
            new_name +=sent[num]
    return new_name

check = old_macdonalt('macdonald')
print(check)


#2................MASTER YODA: Given a sentence, return a sentence with the words reversed
def master_yoda(text):
    my_text=' '
    for char in text.split():
        my_text = " " +char +my_text
    return my_text.lstrip()

check =master_yoda('I am home')
print(check)
check =master_yoda('We are ready')
print(check)



# 3........ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
#The phrase "almost there" means that a number is close to a given target. In this case, we are checking if a number n is close to 100 or 200, specifically within 10 units of these values.

def almost_there(num):
    #Num should be 10 units either away or close the 100 or 200
    if num in range(90, 111) or num in range(190, 121):
        return True
    else:
        return False

check= almost_there(150)
print(check)
check= almost_there(104)
print(check)
check= almost_there(90)
print(check)



print('----------------level 2---------------------------')
print('1...Given a list of ints, return True if the array contains a 3 next to a 3 somewhere ')
def has_33(mylist):
    #find the first occurrence of 3
    #**find the lenght of the number
    #**break the list: index, value - enumerate()
    #check if the number next to it is 3
    has_found_3 =mylist.index(3)
    for num in range(len(mylist)):

        if has_found_3 and mylist[has_found_3+1]==3:
            return True
        else:
            return False

check = has_33([1, 3, 3])
print(check)
check = has_33([1, 3, 1, 3])
print(check)
check = has_33([3, 1, 3])
print(check)



print('\n\nQ2...PAPER DOLL: Given a string, return a string where for every character in the original there are three characters')
def paper_doll(text):
    mywords= ''
    for char in text:
        mywords += char*3

    return mywords

check =paper_doll('Hello')
print(check)


print("\n\nQ3...BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. \nIf their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'")
def blackjack(a,b,c):
#     Should be between 1 and 11
    total = a +b+c
    checK_num = a == 11 or b==11 or c ==11
    if not(1 <= a <= 11) or not(1 <= a <= 11) or not(1 <= a <= 11):
        return
    # to_list = list(a
    if total <= 21:
        return total
#     return sum: sum <= 21
    elif checK_num and total >21:
        my_reduction = total-10
        if my_reduction <= total:
            return my_reduction
    else:
        return 'BUST'
#     ruturn sum: if sum > 21 and

check =blackjack(5,6,7)
print(check)

check =blackjack(9,9,9)
print(check)

check =blackjack(9,9,11)
print(check)


print("\n\nQ4...Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.")
def summer_69(arr):
    added=0
    for index, num in enumerate(arr):
        if (num==6 and arr[index+1]==9) or (num==9 and arr[index-1]==6):
            continue
        elif num ==6:
            break
        else:
            added +=num

    return added

check= summer_69([1,3,5])
print(check)

check= summer_69([4, 5, 6, 7, 8, 9])
print(check)

check= summer_69([2, 1, 6, 9, 11])
print(check)


print("Q5....COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number")

def count_primes(num):
    