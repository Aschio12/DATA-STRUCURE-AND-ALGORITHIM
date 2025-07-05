for _ in range(int(input())):
    n,a,b=map(int,input().split())
    if n==1:
        print(a)
    elif a*2<=b:
        print(n*a)
    elif n%2!=0:
        print((n//2*b)+a)
    else:
        print(n//2*b)