from collections import defaultdict
class Solution:
    def maxScoreIndices(self, arr: List[int]) -> List[int]:
        d=defaultdict(list)
        left_zero=0
        right_one=arr.count(1)
        summ=left_zero+right_one
        d[summ].append(0)
        for i in range(1,len(arr)+1):
            if arr[i-1]==0:
                left_zero+=1
            else:
                right_one-=1
            if summ<=left_zero+right_one:
                summ=left_zero+right_one
                d[summ].append(i)
        return(d[summ])