"""
recursive binary search actually calls itself after result is not found
"""

def recursive_binary_search(list, target):
    if len(list) == 0:
        return None
    else:
        midpoint = (len(list)) // 2
        if list[midpoint] == target:
            return True
        else:
            # Returning binary set with a copy or slice of the original function
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint + 1:], target)
            else:
                return recursive_binary_search(list[:midpoint], target)


def verify(result):
    print('Target found', result)


result =recursive_binary_search([x for x in range(0,101)], 5)
print(verify(result))