for _ in range(int(input())):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    given=0
    count=0
    for i in arr:
        if i>=k:
            given+=i
        if i==0 and given:
            count+=1
            given-=1
    print(count)