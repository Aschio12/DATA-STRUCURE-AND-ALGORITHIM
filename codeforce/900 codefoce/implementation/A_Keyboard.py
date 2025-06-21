direction=input()
keyboard=list("qwertyuiopasdfghjkl;zxcvbnm,./")
wrong=list(input())
ans=[0]*len(wrong)
for i in range(len(wrong)):
    index=keyboard.index(wrong[i])
    if direction=="R":
        ans[i]=keyboard[index-1]
    else:
        ans[i]=keyboard[index+1]
ans="".join(ans)
print(ans)