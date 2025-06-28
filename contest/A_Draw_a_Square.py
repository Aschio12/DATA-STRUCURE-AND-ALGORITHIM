for _ in range(int(input())):
    arr=list(map(int,input().split()))
    print("YES" if all(a==arr[0] for a in arr) else "NO")