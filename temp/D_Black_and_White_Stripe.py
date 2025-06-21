t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    color=input()
    current=0
    ans=float("inf")
    start=0
    for i in range(len(color)):
        if color[i]=="W":
            current+=1
        if i-start+1==k:
            if color[start]=="W" and n>1:
                current-=1
            start+=1
            if ans>current:
                ans=current
    print(ans) 