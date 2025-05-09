for _ in range(int(input())):
    l=int(input())
    arr=list(map(int,input().split()))
    ans=[]
    l,r=0,len(arr)-1
    left=True
    while l<=r:
        if left:
            ans.append(arr[l])
            l+=1
            left=False
        else:
            ans.append(arr[r])
            r-=1
            left=True
    print(*ans)