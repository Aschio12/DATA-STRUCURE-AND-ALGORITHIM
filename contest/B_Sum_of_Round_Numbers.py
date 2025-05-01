t=int(input())
for _ in range(t):
    num=input()
    p=[]
    for i in range(len(num)):
        h=len(num)-i-1
        if num[i]!="0":
            ans=int(num[i])*(10**h)
            p.append(ans)
        else:
            continue
    print(len(p))
    print(*p)