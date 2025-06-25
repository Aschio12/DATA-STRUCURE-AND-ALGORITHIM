for _ in range(int(input())):
    n=int(input())
    arr=[]
    for i in range(n):
        arr.append(tuple(map(int,input().split())))
    max=0
    for i in range(len(arr)):
        if arr[i][0]<=10:
            if arr[i][1]>max:
                max=arr[i][1]
                ans=i
    print(ans+1)