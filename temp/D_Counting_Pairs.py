for _ in range(int(input())):
    n,x,y=map(int,input().split())
    arr=list(map(int,input().split()))
    count=0
    tot=sum(arr)
    for i in range(n-1):
        for j in range(i+1,n):
            rem_s=tot-(arr[i]+arr[j])
            if x<=rem_s<=y:
                count+=1
            
    print(count)