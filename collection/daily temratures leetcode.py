tem= [30,60,90]
ans=[]
l,r=0,1
while l<len(tem):
    cheacked=tem[l]
    while cheacked>=tem[r]:
        r+=1
        if r>=len(tem):
            r=l
            break
    ans.append(r-l)
    l+=1
    r=l+1
    if r>=len(tem):
        ans.append(0)
        break
print(ans)