interval=[[1,3],[2,6],[8,10],[15,18]]
ans=[]
interval.sort(key=lambda x : x[0])
ans.append(interval[0])
a=0
for i in range(1,len(interval)):
    if interval[i][0]>=ans[a][0] and interval[i][0]<=ans[a][1]:
        ans[a]=[min(interval[i][0],ans[a][0]),max(interval[i][1],ans[a][1])]
    else:
        ans.append(interval[i])
        a+=1
print(ans)