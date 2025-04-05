test=int(input())
ans=[]
for _ in range(test):
    n=int(input())
    pairs=[]
    for b in range(1,n+1):
        a=n-b
        if a==0 :
            break
        else:
            pairs.append((a,b))
    ans.append(len(pairs))
for item in ans:      
    print(item)