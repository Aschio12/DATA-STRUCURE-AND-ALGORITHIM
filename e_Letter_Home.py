for _ in range(int(input())):
    n,s=map(int,input().split())
    arr=list(map(int,input().split()))
    p1=min(abs(arr[0]-s),abs(arr[-1]-s))
    store=[]
    for i in range(1,n):
        store.append(arr[i]-arr[i-1])
    tot=sum(store)+p1
    print(tot)