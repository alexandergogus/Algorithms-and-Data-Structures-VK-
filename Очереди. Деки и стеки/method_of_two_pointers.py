from collections import deque

def is_Subsequence(a, b):
    deque_a = deque(a)
    deque_b = deque(b)
    pointer_a, pointer_b = 0,0
    while pointer_b < len(deque_b) and pointer_a < len(deque_a):
        if deque_a[pointer_a] == deque_b[pointer_b]:
            pointer_a += 1
        pointer_b += 1
    return pointer_a == len(deque_a)

word1 = 'abd'
word2 = 'uabqd'
print(is_Subsequence(word1,word2))