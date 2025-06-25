for _ in range(int(input())):
    n=int(input())
    a=input()
    b=input()
    check1=""
    check2=""
    for i,j in zip(a,b):
        if i=="G":
            check1+="B"
        else:
            check1+=i
        if j=="G":
            check2+="B"
        else:
            check2+=j
    print("YES" if check1==check2 else "NO")
            