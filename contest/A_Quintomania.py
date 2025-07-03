for _ in range(int(input())):
    def f():
        n=int(input())
        arr=list(map(int,input().split()))
        for i in range(1,len(arr)):
            if abs(arr[i]-arr[i-1])!=5 and abs(arr[i]-arr[i-1])!=7:
                return("NO")
        return("YES")
    print(f())