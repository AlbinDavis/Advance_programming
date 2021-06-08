# The problem is to count all the possible paths from top left to bottom right of a MxN matrix with the constraints that from each cell you can either move to right or down.

# Example 1:

# Input:
# M = 3 and N = 3
# Output: 6
# Explanation:
# Let the given input 3*3 matrix is filled 
# as such:
# A B C
# D E F
# G H I
# The possible paths which exists to reach 
# 'I' from 'A' following above conditions 
# are as follows:ABCFI, ABEHI, ADGHI, ADEFI, 
# ADEHI, ABEFI


import math
def numberOfPaths (self, n, m):
    return math.factorial(m+n-2)//(math.factorial(n-1)*math.factorial(m-1))
