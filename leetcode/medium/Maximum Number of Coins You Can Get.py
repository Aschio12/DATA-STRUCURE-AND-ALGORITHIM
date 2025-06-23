class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        n=len(piles)-1
        i=1
        ans=[]
        while i<n:
            ans.append(piles[i])
            i+=2
            n-=1
        return(sum(ans))