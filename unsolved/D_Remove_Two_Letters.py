for _ in range(int(input())):
    n=int(input())
    st=input()
    stor=set()
    for i in range(len(st)-1):
        r=i+1
        temp=tuple(st[:i]+st[i+1:r]+st[r+1:])
        stor.add(temp)
    print(len(stor))
        