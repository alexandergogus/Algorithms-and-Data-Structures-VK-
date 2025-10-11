import random

def create_array(n):
    array = []
    for i in range(n):
        random_integer = random.randint(1, 100)
        array.append(random_integer)
    return array

def reverse_array(array):
    left = 0
    right = len(array)-1
    while left < right :
        array[left], array[right] = array[right], array[left]
        left = left + 1
        right = right - 1
    return array

n = int(input("How many elements in massive? "))
massive = create_array(n)
print(massive)
print(reverse_array(massive))