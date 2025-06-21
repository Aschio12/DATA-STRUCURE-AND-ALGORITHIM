for _ in range(int(input())):
    input()
    k,n,m=map(int,input().split())
    nn=list(map(int,input().split()))
    mm=list(map(int,input().split()))
    oo=nn+mm
    ma=max(oo)
    z=oo.count(0)
    ans=[0]*(n+m)
    def f():
        i=0
        global k,n,m
        while i<=k:
            if ma>k+z:
                return(-1)
            if oo[i]==0:
                k+=1
            elif oo[i]>k:
                i+=1
            else:
                ans[i]=oo[i]
                oo.remove(oo[i])
                i-=1
        return(ans)
    print(f())