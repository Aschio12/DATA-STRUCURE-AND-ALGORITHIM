for _ in range(int(input())):
    tic=list(map(int,list(input())))
    if sum(tic[:3])==sum(tic[3:6]):
        print("YES")
    else:
        print("NO")