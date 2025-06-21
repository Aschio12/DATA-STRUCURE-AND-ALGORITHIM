from collections import defaultdict
strs=["eat","tea","tan","ate","nat","bat"]
d=defaultdict(list)
for s in strs:
    anag=tuple(sorted(s))
    d[anag].append(s)
print(list(d.values()))