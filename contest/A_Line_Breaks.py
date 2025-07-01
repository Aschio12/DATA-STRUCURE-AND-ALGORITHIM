for _ in range(int(input())):
    s,m=map(int,input().split())
    arr=[input() for _ in range(s)]
    index,tot=0,0
    while tot<m and index<len(arr):
        tot+=len(arr[index])
        index+=1
    print(index if tot<=m else index-1)
