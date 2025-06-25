t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    sum_even = 0
    sum_odd = 0
    for num in arr:
        if num % 2 == 0:
            sum_even += num
        else:
            sum_odd += num
    if sum_even > sum_odd:
        print("YES")
    else:
        print("NO")