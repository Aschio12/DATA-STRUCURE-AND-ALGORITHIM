test=int(input())
for _ in range(test):
    l=int(input())
    number=list(map(int,input().split()))
    number.sort()
    count=1
    for i in range(1,len(number)):
        if number[i]==number[i-1]:
            count+=1
            if count==3:
                print(number[i])
                break
           
        else:
            count=1
    if count<3:
        print(-1)
    
    