def check_palindrom(word):
    left = 0
    right = len(word)-1
    while left < right:
        if word[left] == word[right]:
            left = left + 1
            right = right - 1
        else:
            return False
    return True

s = str(input())
print(check_palindrom(s))