test=int(input())
for i in range(test):
    inter=input()
    a=list(inter[:3])
    b=list(inter[4:])
    a[0],b[0]=b[0],a[0]
    print("".join(a),"".join(b))

