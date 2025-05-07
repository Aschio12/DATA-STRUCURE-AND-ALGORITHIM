costs = [10,6,8,7,7,8]
coins = 5
costs.sort()
req,count=0,0
for i in costs:
    req+=i
    if req<=coins:
        count+=1
print(count)