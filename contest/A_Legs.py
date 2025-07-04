import math
for _ in range(int(input())):
    leg=int(input())
    if leg==2:
        print(1)
    elif leg%4==0:
        print(int(leg/4))
    elif leg>4 and leg%4!=0:
        print(int(math.floor(leg/4)+1))
        