class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        nums1=list(set(nums1))
        nums2=list(set(nums2))
        l=max(len(nums1),len(nums2))
        if len(nums1)==l:
            cheacker=nums1
        else:
            cheacker=nums2
        for i in cheacker:
            if i in nums1 and i in nums2:
                ans.append(i)
        return(ans)