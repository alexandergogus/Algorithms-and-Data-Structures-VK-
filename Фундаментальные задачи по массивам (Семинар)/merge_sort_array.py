import random

def create_array(n):
    array = []
    for i in range(n):
        random_integer = random.randint(1, 100)
        array.append(random_integer)
    array.sort()
    return array

def merge_arrays(arr1, arr2):
    index1 = 0
    index2 = 0
    merge = []
    while(index1 < len(arr1)) and (index2 < len(arr2)):
        if arr1[index1] > arr2[index2]:
            merge.append(arr2[index2])
            index2 = index2 + 1
        else:
            merge.append(arr1[index1])
            index1 = index1 + 1

    merge.extend(arr1[index1:])
    merge.extend(arr2[index2:])
    return merge

n = 5
m = 6
list1 = create_array(n)
print(list1)
list2 = create_array(m)
print(list2)
result = merge_arrays(list1, list2)
print(result)