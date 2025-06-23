from collections import Counter
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    store = [arr[i] - i for i in range(n)]
    freq = Counter(store)
    total_pairs = sum(v * (v - 1) // 2 for v in freq.values() if v >= 2)
    print(total_pairs)
