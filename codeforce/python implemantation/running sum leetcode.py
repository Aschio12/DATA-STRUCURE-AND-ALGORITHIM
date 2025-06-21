nums=[1,2,3]
current_sum=0
running_sum=[]
for i in range(len(nums)):
    current_sum+=nums[i]
    running_sum.append(current_sum)
print(running_sum)
