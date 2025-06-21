for _ in range(int(input())):
    length,changes=map(int,input().split())
    arr=list(map(int,input().split()))
    prefix=[0]*(length+1)
    for i in range(len(prefix)):
        prefix[i+1]=arr[i]+prefix[i]
    for i in range(changes):
        l,r,k=map(int,input().split())
        
        if temp%2==1:
            print("YES")
        else:
            print("NO")
