for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    ans=[]
    l,r=0,1
    while l<n-1:
        if arr[r]-arr[l]==r-l:
            ans.append((l,r))
        r+=1
        if r==n:
            l+=1
            r=l+1
    print(len(ans))