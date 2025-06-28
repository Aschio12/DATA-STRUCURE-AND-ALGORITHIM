from collections import defaultdict
for _ in range(int(input())):
    def f():
        nn=int(input())
        a=list("01032025")
        n=input().split()
        count=0
        for i in n:
            if i in a:
                a.remove(i)
            count+=1
            if len(a)==0:
                return(count)
        return 0
        
    print(f())