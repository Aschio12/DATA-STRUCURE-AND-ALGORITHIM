for _ in range(int(input())):
    def f():
        p=input()
        s=input()
        pp=0
        ss=0
        n=len(p)
        m=len(s)
        while pp<n and ss<m:
            point=p[pp]
            count_p=0
            count_s=0
            while pp<n and point==p[pp]:
                count_p+=1
                pp+=1
            while ss<m and point==s[ss]:
                count_s+=1
                ss+=1
            if count_s>2*count_p or count_p>count_s:
                return("NO")       
        if pp<n or ss<m:
            return("NO")
        return("YES")
    print(f())
        