test=int(input())
for _ in range(test):
    l=int(input())
    ab=input()
    a=list(ab)
    a.sort()
    a.reverse()
    ans=ord(a[0])-ord("a")+1
    print(ans)