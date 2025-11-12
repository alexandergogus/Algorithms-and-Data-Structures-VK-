def group_anagrams(data):
    groups = {}
    for i in range (len(data)):
        key = ''.join(sorted(data[i]))
        if key not in groups:
            groups[key] = []
        groups[key].append(data[i])
    return list(groups.values())

print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
print(group_anagrams(["won","now","aaa","ooo","ooo"]))
