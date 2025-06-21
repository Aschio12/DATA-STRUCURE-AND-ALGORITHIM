n=int(input())
key_dor=input()
count=0
check=[]
for i in range(0,len(key_dor),2):
    if key_dor[i].upper()!=key_dor[i+1]:
        if key_dor[i+1].lower() not in check:
            count+=1
            check.append(key_dor[i])
    elif key_dor[i].upper()!=key_dor[i+1] and key_dor[i+1].lower() in check:
        check.remove(key_dor[i])
print(count)
