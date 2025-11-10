def find_sqrt(x):
    if x < 0:
        return None
    if x == 0 or x == 1:
        return x

    left = 0
    right = x
    while left<=right:
        middle = (left+right)//2
        if middle**2 > x:
            right = middle - 1
        if middle**2 < x:
            left = middle + 1
        if middle**2 == x:
            return middle

    if (left**2 - x) < (- right**2 + x):
        return left
    else:
        return right

x = int(input())
print(find_sqrt(x))