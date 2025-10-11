import random

def create_array(n):
    array = []
    for i in range(n):
        random_integer = random.randint(1, 100)
        array.append(random_integer)
    array.sort()
    return array

def two_sum_function(array, target):
    left = 0
    right = len(array)-1
    while left < right:
        if array[left] + array[right] == target:
            return left, right
        elif array[left] + array[right] > target:
            right = right - 1
        else:
            left = left + 1
    return 0

n = int(input("How many elements in massive? "))
target = int(input("What is the target?"))
massive = create_array(n)

answer = two_sum_function(massive, target)
print(massive)
if answer == 0:
    print("There is no such pair!")
else:
    print(answer)