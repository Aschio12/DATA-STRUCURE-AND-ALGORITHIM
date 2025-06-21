import math
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    tp=arr.copy()
    for i in range(1,n+1):
        tp[i-1]=(i,arr[i-1])
    for t in tp:
        gcd=math.gcd(t[0],t[1])
        if gcd==1:
            print(n-t[1]+1)
            break