# There is a tournament between two teams. The tournament consists of N rounds. Each team has N competitors. Each competitor has a power between a-z and if the power of two competitors matches in a round then that round will going to be drawn. You have to find the maximum number of draw rounds possible.

# Input Format:

# The first line of input contains T, denotes the total number of test cases.

# Each test case contains an Integer N denotes the number of rounds.

# Next two lines will contain a string of lowercase letters of length N denoting the power of N competitors of both teams.

# Output Format:

# Output the answer in a new line.

# Constraints:

# 1 <= T <= 10
# 1 <= N <= 105 
# String will contain only lowercase alphabet
# SAMPLE INPUT 
# 2
# 4
# aabc
# zcaa
# 5
# pqrrs
# rsptr

# SAMPLE OUTPUT 
# 3
# 4

from collections import Counter as co

def check(n1,n2):
    c=0
    n2=co(n2)
    for i in n1:
        if i in n2 and n2[i]!=0:
            c+=1
            n2[i]-=1
    return(c)
    

t=int(input())
lis=[]
for i in range(t):
    k=int(input())
    n1=list(input())
    n2=list(input())
    print(check(n1,n2))
