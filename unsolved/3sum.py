nums = [-1,0,1,2,-1,-4]
ans=[]
for i in range(len(nums)-2):
    for  j in range(i+1,len(nums)-1):
        for k in range(j+1,len(nums)):
            zero=nums[i]+nums[j]+nums[k]
            if zero==0:
                ap=sorted([nums[i],nums[j],nums[k]])
                if ap not in ans:
                    ans.append(ap)
print(ans)

         
            