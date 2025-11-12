def target_sum_search(data, target):
    cache = {}
    for i in range (len(data)):
        delta = target - data[i]
        if delta in cache:
            return [cache[delta], i]
        cache[data[i]] = i
    return []

target = int(input())
n = int(input())
data = []
for i in range(n):
    element = int(input())
    data.append(element)

print(target_sum_search(data, target))