class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        m=len(matrix[0])
        r_zero=[]
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    r_zero.append((i,j))
        for i in r_zero:
            matrix[i[0]]=[0]*m
            for j in range(n):
                matrix[j][i[1]]=0
                
                        