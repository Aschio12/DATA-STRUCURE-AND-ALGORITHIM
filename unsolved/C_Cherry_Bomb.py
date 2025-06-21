for _ in range(int(input())):
    def f():
        n,k=map(int,input().split())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        minus=b.count(-1)
        m=max(a)
        d=min(a)
        check=[]
        if any(num>k for num in a) or any(num>k for num in b):
            return 0
        for aa,bb in zip(a,b):
            if bb!=-1:
                c=aa+bb
                check.append(c)
                if c<m or c>k:
                    return 0
        if any(num!=check[0] for num in check):
            return 0
        if minus==n:
            ans=k-m+d+1
        else:
            ans=1
        return ans
    print(f())
             
        