for _ in range(int(input())):
    num = list(map(int, input()))
    num.sort(reverse=True)
    sl = 0
    ans = []
    for i in range(9,-1,-1):  
        cheack = [x for x in num if x >= i] 
        if len(cheack)>=1:
            ans.append(min(cheack))
            num.remove(min(cheack))
        ans=list(map(str,ans))
        p="".join(ans)
    print(p)
