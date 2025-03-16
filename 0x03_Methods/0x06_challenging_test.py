print("Q1:---SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order---------------")
def spy_game(nums):
    count =[0,0,7, 'x']
    for num in nums:
        if num == count[0]:
            count.pop(0)
    return  len(count)==1

check =spy_game([1,2,4,0,0,7,5])
print(check)
check =spy_game([1,0,2,4,0,5,7])
print(check)
check =spy_game([1,7,2,0,4,5,0])
print(check)

come =[1,2,3,4]
print(come.pop(0))


print("Q-: Write a function that returns the number of prime numbers that exist up to and including a given number")
def count_primes2(num):
    primes = [2]
    x = 3
    if num < 2:
        return 0
    while x <= num:
        for y in primes:  # use the primes list!
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)


check = count_primes2(100)
count_primes2(100)
print(check)
print('hi')


def print_big(letter):
    patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    '}
    alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])

car= print_big('A')
print(car)
