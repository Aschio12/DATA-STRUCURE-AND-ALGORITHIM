for _ in range(int(input())):
    n=int(input().strip())
    store=[input() for _ in range(n)]
    cols=[]
    for i in range(n-1,-1,-1):
        cols.append(store[i].index("#")+1)
    print(*cols)