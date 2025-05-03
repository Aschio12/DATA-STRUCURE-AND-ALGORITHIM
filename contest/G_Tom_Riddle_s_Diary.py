a=[]
for _ in range(int(input())):
    b=input()
    if b in a:
       print("YES")
    else:
        a.append(b)
        print("NO")
    