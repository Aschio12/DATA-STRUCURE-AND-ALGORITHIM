for _ in range(int(input())):
    n,x=map(int,input().split())
    arr=list(map(int,input().split()))
    arr.sort(reverse=True)
    l,r,count=0,0,0
    while r<n:
        strength=arr[r]*(r-l+1)
        if strength>=x:
            count+=1
            l=r+1
            r=l
        else:
            r+=1
    print(count)