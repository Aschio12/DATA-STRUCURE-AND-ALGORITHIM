accounts = [[1,2,3],[3,2,1]]
current_max,b=0,0
for balance in range(len(accounts)):
    b=sum(accounts[balance])
    if current_max<b:
        current_max=b
print(current_max)