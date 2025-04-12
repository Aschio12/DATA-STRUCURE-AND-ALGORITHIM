test=int(input())
ans=[]
for _ in range(test):
    current_min= float('inf')
    a,b=map(int,input().split())
    for c in range(a,b+1):
        mini=(c-a)+(b-c)
        if a==b:
            current_min=0
            break
        else:
            if mini<current_min:
                current_min=mini
    ans.append(current_min)
for i in ans:
    print(i)



