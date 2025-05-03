from collections import Counter
for _ in range(int(input())):
    l=int(input())
    s=list(map(int,input().split()))
    a=list(Counter(s).values())
    coun=0
    print(len(a))