def findRotation(mat, target):
    n = len(mat)
    if mat == target:
        return True
        
    def rotate90(matrix):
        n_val = len(matrix)
        rotated = [[0] * n_val for _ in range(len(matrix[0]))]
        for i in range(n_val):
            for j in range(n_val):
                rotated[i][j] = matrix[n_val - 1 - j][i]
        return rotated

    current = mat
    for _ in range(3):
        current = rotate90(current)
        if current == target:
            return True
            
    return False
print(findRotation(mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]))