s,n=map(int,input().split())
store=[0]*n
for i in range(n):
    x,y=map(int,input().split())
    store[i]=(x,y)
store.sort(key=lambda z:z[0])
def name():
    global s
    global n
    for xy in store:
        if xy[0]<s:
            s+=xy[1]
        else:
            return("NO")
    return("YES")
print(name())
