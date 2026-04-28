
def _main():
    
    numbers = [2, 4, 6, 8, 10, 12, 14]

    print(binary_search(numbers, 10))  # 4
    print(binary_search(numbers, 5))   # -1
    
    print(binary_search_recursive(numbers, 10))  # 4
    print(binary_search_recursive(numbers, 5))   # -1

def binary_search(values, target):
    """
    Return the index of target in values if found.
    Return -1 if target is not found.

    values must be sorted.
    """
    left = 0
    right = len(values) - 1

    while left <= right:
        middle = (left + right) // 2

        if values[middle] == target:
            return middle
        elif values[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1

def binary_search_recursive(values, target, left=0, right=None):
    """
    Return the index of target in values if found.
    Return -1 if target is not found.

    values must be sorted.
    """
    if right is None:
        right = len(values) - 1

    # Base case: search space is empty
    if left > right:
        return -1

    middle = (left + right) // 2

    if values[middle] == target:
        return middle
    elif values[middle] < target:
        return binary_search_recursive(values, target, middle + 1, right)
    else:
        return binary_search_recursive(values, target, left, middle - 1)
    
_main()