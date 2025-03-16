print("Q1")
print('here is the question: you are given an array of intergers a and an interger k, \nYour task is to " calculate the number of ways to pick two different indices i< j such that a[i] +a[j] is divisible by k \neg. a [1,2,3,4,5] and k=3, the output should be solution(a,k)=4')

def solution(a, k):
    count = 0
    n = len(a)

    for i in range(n):
        for j in range(i + 1, n):  # Ensure i < j
            if (a[i] + a[j]) % k == 0:
                count += 1

    return count


# Test case
print(solution([21, 20, 19, 34, 23, 35], 3))  # Expected Output: 4

check =solution([1,2,3,4,5],3)
print(check)

print(int(6%3))



print('Q2')
print("RLE works by taking the occurrence of eact repeating character and outputting that number along with a single character of the repeating sequence.\n For inputString ='aabbaaac', the output shoould be \nsolution(inputString)='1a2b4a1c")


def input_solution(inputString):
    if not inputString:  # Handle empty string case
        return ""

    count_char = ""
    counting = 1  # To count occurrences of each character

    for i in range(len(inputString) - 1):  # Loop till second last character
        if inputString[i] == inputString[i + 1]:
            counting += 1  # Increase count if next char is the same
        else:
            count_char += f"{counting}{inputString[i]}"  # Store count + character
            counting = 1  # Reset count for the new character

    # Add last character count (since it won't be added in loop)
    count_char += f"{counting}{inputString[-1]}"

    return count_char


# Test cases
print(input_solution("abbcccddddd"))  # Expected: "1a2b3c5d"
print(input_solution("aaabbc"))  # Expected: "3a2b1c"
print(input_solution(""))  # Expected: ""
print(input_solution("abc"))  # Expected: "1a1b1c"

# count_char = count_char + f'{counting}{inputString[i]}'
    #     print(count_char)


check = input_solution("abbcccddddd")
print(check)