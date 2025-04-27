t=int(input())
for _ in range(t):
    w=input()
    if w[0]+w[1]+w[2]=="abc" or w[0]+w[2]+w[1]=="abc" or w[1]+w[0]+w[2]=="abc" or w[2]+w[1]+w[0]=="abc":
        print("YES")
    else:
        print("NO")
        