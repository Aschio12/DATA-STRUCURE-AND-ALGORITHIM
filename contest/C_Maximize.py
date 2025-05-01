import math
t=int(input())
for _ in range(t):
    x=int(input())
    ans,p=0,0
    for y in range(1,x):
        gcd=math.gcd(x,y)
        tot=gcd+y
        if tot>ans:
            ans=tot
            p=y
    print(p)
        
        
    