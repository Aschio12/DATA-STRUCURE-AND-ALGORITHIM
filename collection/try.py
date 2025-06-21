def f():
    p="001011"
    t="10010101101001100101111010"
    m=len(p)
    n=len(t)
    for i in range(n-m):
        j=0
        while j<m and p[j]==t[i+j]:
            j+=1
        if j==m:return i
    return -1
print(f())