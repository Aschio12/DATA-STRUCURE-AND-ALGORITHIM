for _ in range(int(input())):
    l=int(input())
    s=list(input())
    if sorted(s)==s:
        print("YES")
    else:
        print("NO")