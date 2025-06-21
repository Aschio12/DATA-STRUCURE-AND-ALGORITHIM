for _ in range(int(input())):
    n,x=map(int,input().split())
    arr=list(map(int,input().split()))
    start=arr.index(1)
    end=0
    for i in range(len(arr)):
        if arr[i]==1:
            end=i
    print("YES" if end-start+1<=x else "NO")