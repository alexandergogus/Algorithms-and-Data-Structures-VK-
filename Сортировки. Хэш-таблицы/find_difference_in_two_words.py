def difference(a,b):
    char_data = {}
    for char in b:
        char_data[char] = char_data.get(char,0)+1

    for char in a:
        char_data[char] = char_data.get(char, 0) - 1

    for char,count in char_data.items():
        if count != 0:
            return char
    return ""

a = str(input())
b = str(input())
print(difference(a,b))