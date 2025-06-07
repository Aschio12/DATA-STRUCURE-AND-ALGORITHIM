for _ in range(int(input())):
    n = int(input().strip())
    arr = list(map(int, input().split()))
    s0 = abs(arr[0])
    L = 0
    for i in range(1, n):
        if abs(arr[i]) < s0:
            L += 1
    k = (n + 1) // 2
    if L <= (k - 1) or L <= (n - k):
        print("YES")
    else:
        print("NO")