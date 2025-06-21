test=int(input())
name=sorted(list("Timur"))
for i in range(test):
    length=int(input())
    permutaion=sorted(list(input()))
    if name==permutaion:
        print("YES")
    else:
        print("NO")