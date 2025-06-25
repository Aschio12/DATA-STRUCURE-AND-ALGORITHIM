for _ in range(int(input())):
    n,k=map(int,input().split())
    keys=list(map(int,input().split()))
    store=[]
    for i in range(n):
        if keys[i]==1:
            store.append(i)
    fidx=store[0]
    lidx=store[-1]
    if lidx-fidx<k:
        print("YES")
    else:
        print("NO")