for _ in range(int(input())):
    n, k, q = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = 0
    current = 0
    for num in arr:
        if num <= q:
            current += 1
        else:
            current = 0
        if current >= k:
            ans += current - k + 1
    print(ans)