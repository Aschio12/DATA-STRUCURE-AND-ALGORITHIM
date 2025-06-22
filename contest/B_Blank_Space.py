for _ in range(int(input())):
    def f():
        n=int(input())
        arr=list(map(int,input().split()))    
        store=[]
        count=0
        for i in range(len(arr)):
            if arr[i]==0:
                count+=1
                if i==n-1:
                    store.append(count)
            else:
                if count not in store:
                    store.append(count)
                count=0
        if store:
            print(max(store))
        else:
            print(0)
    f()