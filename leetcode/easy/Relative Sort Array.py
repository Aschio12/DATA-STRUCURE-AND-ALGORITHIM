class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        m=max(arr1)+1
        count=[0]*m
        ans=[]
        for i in range(len(arr1)):
            count[arr1[i]]+=1
        for i in arr2:
            ans.extend([i]*count[i])
        for i in range(m):
            if i not in ans:
                ans.extend([i]*count[i])
        return ans
    