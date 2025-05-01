t=int(input())
for _ in range(t):
    inp=list(map(int,input().split()))
    inp.sort()
    m=max(inp)
    c=inp.count(m)
    if c>1:
        ans=(inp[0]+5)*(inp[2]*2)
    elif inp[0]==inp[1]==inp[2]:
        ans=((inp[0]+2)*2)*(inp[0]+1)
    else:
        ans=(inp[0]+3)*(inp[1]+2)*(inp[2])
    print(ans)
        