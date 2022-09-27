def binary_search(list, target):
    first = 0
    last = len(list) - 1
    while first <= last:
        midpoint = (first + last) // 2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None


def recursive_binary_search(list, target):
    midpoint = len(list) // 2
    if len(list) == 0:
        return False
    else:
        if list[midpoint] == target:
            return True
        elif list[midpoint] < target:
            return recursive_binary_search(list[midpoint + 1:], target)
        else:
            return recursive_binary_search(list[:midpoint], target)


def verify(result):
    print("Target found: ", result)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
result = binary_search(numbers, 1)
verify(result)

result = recursive_binary_search(numbers, 4)
verify(result)

from timeit import default_timer as timer
from datetime import timedelta

start = timer()

end = timer()
print(timedelta(seconds=end - start))
