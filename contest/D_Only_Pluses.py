for _ in range(int(input())):
    a,b,c=map(int,input().split())
    current_max=0
    for i in range(6):
        for j in range(6-i):
            for k in range(6-i-j):
                new_a=a+i
                new_b=b+j
                new_c=c+k
                pro=new_a*new_b*new_c
                current_max=max(current_max,pro)
    print(current_max)
            