def transpose(m):
    res = [[0,0],[0,0],[0,0]]
    for i in range(len(m)):
        for j in range(len(m[0])):
            res[j][i] = m[i][j]
    return res
print(transpose([[1,2,3],[4,5,6]]))