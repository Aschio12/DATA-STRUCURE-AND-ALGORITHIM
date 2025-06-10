for _ in range(int(input())):
    def f():
        x,y,a=map(int,input().split())
        l=x+y
        min_=(a//l)*l
        remainder=a-min_
        if x>a:
            return("NO")
        if y>a:
            return("YES")
        if (x>=remainder+0.5):
            return("NO")
        else:
            return("YES")
    print(f())
            