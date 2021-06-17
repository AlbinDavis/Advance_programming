
# Given a string of odd length, print the string X format.
# Examples : 

# Input: 12345
# Output:
# 1       5
#   2   4
#     3
#   2   4
# 1       5

s="geekss"
for i in range(len(s)):
    j=len(s)-i-1
    for k in range(len(s)):
        if k is i or k is j:
            print(s[k],end="")
        else:
            print(" ",end="")
    print()
        
