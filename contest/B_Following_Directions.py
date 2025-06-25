for _ in range(int(input())):
    n=int(input())
    s=input()
    start=[0,0]
    target=[1,1]
    def f():
        for i in s:
            if i=="L":
                start[0]-=1
            elif i=="R":
                start[0]+=1
            elif i=="U":
                start[1]+=1
            elif i=="D":
                start[1]-=1
            if start==target:
                return "YES"
        return "NO"
    print(f())