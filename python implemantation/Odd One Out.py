test=int(input())
for _ in range(test):
    number=list(map(int,input().split()))
    hash={}
    for i in range(len(number)):
        if number[i] in hash:
            hash[number[i]]+=1
        else:
            hash[number[i]]=1
    for key,value in hash.items():
        if value==1:
            print(key)
           