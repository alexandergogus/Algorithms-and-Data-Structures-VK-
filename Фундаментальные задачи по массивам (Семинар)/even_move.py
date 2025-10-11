import random

def create_array(n):
    array = []
    for i in range(n):
        random_integer = random.randint(0, 100)
        array.append(random_integer)
    return array

def even_move(arr):
    even_point = 0
    for i in range (len(arr)):
        if arr[i]%2 == 0:
            arr[i], arr[even_point] = arr[even_point], arr[i]
            even_point = even_point + 1
    return arr

m = 10
massive = create_array(m)
print(massive)
massive = even_move(massive)
print(massive)