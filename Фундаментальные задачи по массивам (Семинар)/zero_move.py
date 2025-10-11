import random

def create_array(n):
    array = []
    for i in range(n):
        random_integer = random.randint(0, 5)
        array.append(random_integer)
    return array

def zero_move(arr):
    point = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[point] = arr[point], arr[i]
            point = point + 1

    for i in range(point, len(arr)):
        arr[i] = 0

    return arr

m = 10
massive = create_array(m)
print(massive)
massive = zero_move(massive)
print(massive)