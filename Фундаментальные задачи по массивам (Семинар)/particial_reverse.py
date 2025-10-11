import random

def create_array(n):
    array = []
    for i in range(n):
        random_integer = random.randint(1, 100)
        array.append(random_integer)
    array.sort()
    return array

def reverse_array(array, left, right):
    while left < right:
        array[left], array[right] = array[right], array[left]
        left = left+1
        right = right - 1
    return array

def part_reverse(array, k):
    k = k % len(array)
    n = len(array)
    array = reverse_array(array, 0, n-1)
    array = reverse_array(array, 0, k-1)
    array = reverse_array(array, k, n-1)
    return array

n = 7
k = 3
massive = create_array(n)
print(massive)
result = part_reverse(massive, k)
print(result)