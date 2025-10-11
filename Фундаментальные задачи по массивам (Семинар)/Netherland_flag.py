import random

def create_array(n):
    array = []
    for i in range(n):
        random_integer = random.randint(0, 2)
        array.append(random_integer)
    return array

def netherland_sort(array):
    low = 0
    mid = 0
    high = len(array)-1
    while mid<=high:
        if array[mid] == 0:
            array[low], array[mid] = array[mid], array[low]
            mid = mid+1
            low = low+1
        elif array[mid] == 1:
            mid = mid+1
        else:
            array[high], array[mid] = array[mid], array[high]
            high = high - 1
    return array

m = 10
massive = create_array(m)
print(massive)
massive = netherland_sort(massive)
print(massive)