import copy
matrix=[[1,2,3],[4,5,6],[7,8,9]]
a=copy.deepcopy(matrix)
for i in range(len(a)):
    for j in range(len(a)):
        matrix[i][j]=a[j][len(a)-1-i]
print(matrix)



