class Solution:
    def reverseWords(self, s: str) -> str:
            ss=s.strip()
            arr=ss.split()
            arr=arr[::-1]
            arr=" ".join(arr)
            return(arr)