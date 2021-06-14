#Given a string S. Count the characters that have ‘N’ number of occurrences. If a character appears consecutively it is counted as 1 occurrence.
# Input:
# S = "abc", N = 1
# Output: 3
# Explanation: 'a', 'b' and 'c' all have 
# 1 occurrence.

# â€‹Example 2:

# Input: 
# S = "geeksforgeeks", N = 2
# Output: 4
# Explanation: 'g', 'e', 'k' and 's' have
# 2 occurrences.

from collections import Counter
S="geeksforgeeks"
l=[]
N=2
if N==0:
    c=0
    k=['a','b','c','d','e','f','g','h','i','j','k','l',
       'm','n','o','p','q','r','s','t','u','v','w','x','y','z']
    d=Counter(S)
    for i in k:
        if i not in d:
            c+=1
else:
    for i in range(len(S)-1):
        if S[i]!=S[i+1]:
            l.append(S[i])
    l.append(S[i+1])
    c=0
    print(l)
    d=Counter(l)
    for i in d:
        if d[i]==N:
            c+=1
print(c)
