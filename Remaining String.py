# Given a string S without spaces, a character ch, and an integer count, the task is 
# to find the string after the specified character has occurred count number of times.

# Example 1:

# Input:  S = "Thisisdemostring", ch = 'i', 
# count = 3
# Output: ng
# Explanation: Substring of S after the 3rd
# occurrence of 'i' is "ng"
# Example 2:

# Input:  S = "Thisisdemostri", ch = 'i', 
# count = 3
# Output: Empty string
# Explanation: 'i' occurce 3rd time at 
# last index

def printString(self, s, ch, count):
  if s.count(ch)<count:
      return "Empty string"
  elif count==0:
            return s

    c=0
    for i in range(len(s)):
        if s[i]==ch:
            c+=1
        if c==count:
            if s[i+1:]:
                return s[i+1:]
            else:
              return "Empty string"
