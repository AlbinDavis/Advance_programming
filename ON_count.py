# There is a row of LED lights aligned in a row and numbered consecutively starting from 1. Each of the LED lights is initially in its "OFF" position. Over some number of operations, a left and right index will be provided. When a current is applied to two LED lights, a NOT operation is applied to each LED light in the inclusive interval between those lights.
# That is, if a light is OFF, it is turned ON, a vice versa. Given a series of operations, determine their final state. Calculate the sum of all indices where light is ON.
# Exemple
# operations[[1,4],[2, 6],[1, 6]]
# 3 operations are performed on a row of LED lights that are all OFF initially. In the figure below, represents a light that is OFF, and an 'X' represents one that is ON.
# After all operations, there are lights in the ON position at indices 2, 3 and 4. The sum of the indices is 2+3+4= 9.
# Function Description
# Complete the function endGame in the editor below. The function must return an integer.
# endGame has the following parameter(s):
# int operations[q][2]- The ith element contains the inclusive range of indices for the th operation.


l=[]
operations=[[9,9],[2,8],[2,3],[10,10],[7,7],[3,4]]
op=0
for i in range(len(operations)):
    if operations[i][1]>op:
        op=operations[i][1]
for i in range(op):
    l.append(0)

for i in range(len(operations)):
    k=operations[i][0]
    while k<=operations[i][1]:
        if l[k-1]==0:
            l[k-1]=1
        else:
            l[k-1]=0
        k+=1
    print(l)
c=0
for i in range(len(l)):
    if l[i]==1:
        c+=i+1
print(c)
        
