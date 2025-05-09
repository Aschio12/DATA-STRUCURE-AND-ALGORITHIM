for _ in range(int(input())):
    length=int(input())
    s=list(input())
    arr=list(map(int,s))
    l,r=0,len(arr)-1
    while l<r and  s[l] != s[r]:
        if l!=r:
            l+=1
            r-=1
    print(r-l+1)