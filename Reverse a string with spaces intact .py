# Given a string, your task is to reverse the string keeping the spaces intact to their positions.

# Example 1:

# Input:
# S = "Help others"
# Output: sreh topleH
# Explanation: The space is intact at index 4
# while all other characters are reversed.
# â€‹Example 2:

# Input: 
# S = "geeksforgeeks"
# Output: skeegrofskeeg
# Explanation: No space present, hence the
# entire string is reversed.

    def reverseWithSpacesIntact(self, s):
        
        l = list(s)
        j= len(s) - 1
        i = 0
        while i<j:
              if l[i]==' ':
                  i+=1
                  continue
              elif l[j]==' ':
                  j-=1
                  continue
              else:
                  l[j],l[i]=l[i],l[j]
                  i+=1
                  j-=1
        return ''.join(l)
