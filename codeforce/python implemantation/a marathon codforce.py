test=int(input())
for _ in range(test):
    distance=list(map(int,input().split()))
    count=0
    for i in range(1,len(distance)):
        if distance[0]<distance[i]:
            count=count+1
    print(count)