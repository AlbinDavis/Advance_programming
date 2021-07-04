# Given a binary matrix your task is to find all unique rows of the given matrix.

# Example 1:

# Input:
# row = 3, col = 4 
# M[][] = {{1 1 0 1},{1 0 0 1},{1 1 0 1}}
# Output: 1 1 0 1 $1 0 0 1 $
# Explanation: Above the matrix of size 3x4
# looks like
# 1 1 0 1
# 1 0 0 1
# 1 1 0 1
# The two unique rows are 1 1 0 1 and
# # 1 0 0 1 


def uniqueRow(row, col, arr):
    s=[]
    l=[]
    for i in range(len(arr)):
        s.append(arr[i])
        if (i+1) % col==0:
            l.append(s)
            s=[]
    for i in l:
        if i not in s:
            s.append(i)
    return s 
