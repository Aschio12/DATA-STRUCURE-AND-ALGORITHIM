nums = [1,2,3,4,5,6,7]
k = 3
for i in range(k):
    tar=nums[-1]
    nums.remove(tar)
    nums.insert(0,tar)
print(nums)