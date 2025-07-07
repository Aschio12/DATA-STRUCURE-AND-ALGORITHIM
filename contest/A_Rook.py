for _ in range(int(input())):
    row="12345678"
    col="abcdefgh"
    pos=input()
    rowpos=[]
    colpos=[]
    for i in range(8):
        ans=col[i]+pos[1]
        if ans !=pos:
            rowpos.append(ans)
    for i in range(8):
        ans=pos[0]+row[i]
        if ans !=pos:
            colpos.append(ans)
    p=rowpos+colpos
    for i in p:
        print(i)