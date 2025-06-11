class Solution:
    def reverse(self, x: int) -> int:
        n=str(x)
        ans=int(n[::-1] if "-" not in n else n[0]+n[1:][::-1])
        return(ans if ans>=-2**31 and ans<=(2**31)-1 else 0)
