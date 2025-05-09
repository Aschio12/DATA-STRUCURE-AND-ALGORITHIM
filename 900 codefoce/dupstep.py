remix=input().split('WUB')
for i in remix:
    if i=="":
        remix.remove(i)
print(*remix)