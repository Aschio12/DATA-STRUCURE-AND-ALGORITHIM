for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,list(input())))
    store=[]
    for i in range(len(arr)):
        to_store=arr[:i]+arr[i:]
        to_store[i]=1 if to_store[i]==0 else 0
        store.append(to_store)
    ans=[]
    for i in store:
        ans+=i
    print(sum(ans))