#1.     Use for, .split(), and if to create a Statement that will print out words that start with 's':
# Variable
mySentence =' Print only the words that start with s in this sentence'
myword= mySentence.lstrip().split(' ')
print(myword)
# For
for word in myword:
# if statement to split
    if word[0]=='s':
        print(word)



#2.    Use range() to print all the even numbers from 0 to 10.
evenPrint = [num for num in range(0,10, 2)]
print(f'Q2: {evenPrint}')



#3. Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
divisibleBy3= [num for num in range(1, 50) if num%3 ==0]
print(f'Q3: {divisibleBy3}')


#4.   Go through the string below and if the length of a word is even print "even!

st = 'Print every word in this sentence that has an even number of letters'
stInBreaks = st.split(" ")
print(stInBreaks)
lenghtOfEvenNum =[length for length in stInBreaks if len(length)%2 ==0]
print(f'Q4: {lenghtOfEvenNum}')


#5.
"""
Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz"""
for num in range(1,101):
    if num% 3==0 and num % 5==0:
        print('FizzBuzz')
    elif num % 3==0:
        print("Fizz")
    elif num% 5 ==0:
        print("Buzz")
    else:
        print(num)



# 6:    Use List Comprehension to create a list of the first letters of every word in the string below:

st = 'Create a list of the first letters of every word in this string'
newSt = st.split(" ")
print(newSt)
myList = [char[0] for char in newSt ]
print(myList)