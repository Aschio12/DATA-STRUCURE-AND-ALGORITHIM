for _ in range(int(input())):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    count=0
    l,r=0,len(arr)-1
    arr.sort()
    while l<r:
        if arr[l]+arr[r]==k:
            count+=1
            l+=1
            r-=1
        elif arr[l]+arr[r]<k:
            l+=1
        else:
            r-=1
    print(count)
            