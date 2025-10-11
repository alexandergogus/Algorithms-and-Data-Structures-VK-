import random

def create_array(n):
    array = []
    for i in range(n):
        random_integer = random.randint(1, 100)
        array.append(random_integer)
    array.sort()
    return array

def add_zeros(arr, m):
    for i in range(m):
        arr.append(0)
    return arr

def merge_upgrade (arr1, arr2):
    pointer1 = len(arr1)-len(arr2)-1
    pointer2 = len(arr2)-1
    pointer3 = len(arr1)-1

    while pointer2 >= 0:
        if pointer1 >= 0 and arr1[pointer1] > arr2[pointer2]:
            arr1[pointer3] = arr1[pointer1]
            pointer1 = pointer1-1
        else:
            arr1[pointer3] = arr2[pointer2]
            pointer2 = pointer2-1
        pointer3 = pointer3-1

    return arr1

n = 4
m = 3
if n > m:
    list1 = create_array(n)
    list1 = add_zeros(list1, m)
    list2 = create_array(m)
    print(list1)
    print(list2)
    list1 = merge_upgrade(list1, list2)
else:
    list1 = create_array(m)
    list1 = add_zeros(list1, n)
    list2 = create_array(n)
    print(list1)
    print(list2)
    list1 = merge_upgrade(list1, list2)

print(list1)