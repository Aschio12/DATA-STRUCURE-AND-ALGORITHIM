from collections import defaultdict
for _ in range(int(input())):
    n,m=map(int,input().split())
    a=input()
    arr=[[]for _ in range(m)]
    for i in range(len(a)):
        j=0
        while j<m:
            if a[i] not in arr[j]:
                arr[j].append(a[i])
                break
            else:
                j+=1
    tot=0
    for i in arr:
        tot+=7-(len(i))
    
    print(tot)
    