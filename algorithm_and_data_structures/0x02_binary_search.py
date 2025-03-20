# Binary Search
def binary_search(list_num, target):
    """
    They must be first sorted: If not, it will return None if value even exist
    We need: first index---> list[0] and last index
    We are using their index not the actual values
    """
    first = 0
    last = len(list_num) - 1
    count = 0

    # This also checks that the list in empty
    # is list is empty: last == -1 which will male the while loop return False
    while first <= last:
        count += 1
        midpoint = (first + last) // 2
        if list_num[midpoint] == target:
            # We are returning the index of the target not the value
            print(f'Number of time it iterated to get the target: {count}')
            return midpoint
        # Change the "first" and "last" values to the  divided part where the target is located
        elif list_num[midpoint] > target:
            # midpoint -1 : midpoint is excluded for now
            last = midpoint-1
        else:
            first = midpoint + 1
    #if target not found
    return None


numbers = [x for x in range(1, 101)]
print(numbers.index(45))
print(binary_search(numbers,45))


nu