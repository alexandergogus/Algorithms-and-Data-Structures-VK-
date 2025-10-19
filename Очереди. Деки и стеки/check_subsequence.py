from collections import deque

def is_Subsequence(a, b):
    deque_a = deque(a)
    deque_b = deque(b)
    for char in deque_b:
        if deque_a and char == deque_a[0]:
            deque_a.popleft()
    return len(deque_a) == 0

word1 = 'abd'
word2 = 'uabqd'
print(is_Subsequence(word1,word2))