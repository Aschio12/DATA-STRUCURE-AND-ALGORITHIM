matrix = [[1,2,3],[4,5,6]]
ans=[[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        ans[j][i]=matrix[i][j]
print(ans)