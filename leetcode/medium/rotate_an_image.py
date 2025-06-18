class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)-1
        temp=[row[:] for row in matrix]
        for row in range(n+1):
            for col in range(n,-1,-1):
                matrix[row][n-col]=temp[col][row]
                        