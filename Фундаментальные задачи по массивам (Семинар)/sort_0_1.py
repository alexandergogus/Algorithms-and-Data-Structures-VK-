import random

def create_array(n):
    array = []
    for i in range(n):
        random_integer = random.randint(0, 1)
        array.append(random_integer)
    return array

def bin_sort(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] == 0:
            left = left+1
        elif arr[right] == 1:
            right = right - 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left = left+1
            right = right-1
    return arr

n = 10
massive = create_array(n)
print(massive)
result = bin_sort(massive)
print(result)