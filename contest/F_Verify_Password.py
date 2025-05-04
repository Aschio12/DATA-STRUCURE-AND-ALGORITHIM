for _ in range(int(input())):
    l=int(input())
    p=list(input())
    d=[]
    a=[]
    for i in p:
        if i.isdigit():
            d.append(i)
        else:
            a.append(i)
    d=list(map(int,d))
    c=''.join(a)
    temp1=a.sort()
    tem2=d.sort()
    if c.lower()!=c:
        print("NO")
    elif a==temp1 and d==tem2:
        p=''.join(p)
        for i in range(1,len(p)):
            if p[i].isdigit() and  p[i-1].isalpha():
                print("NO")
                break 
        print("YES")
                