# Given a string S, find the longest palindromic substring in S. Substring of string S: S[ i . . . . j ] where 0 ≤ i ≤ j < len(S). Palindrome string: A string which
# reads the same backwards. More formally, S is palindrome if reverse(S) = S. Incase of conflict, return the substring which occurs first ( with the least starting index ).
# Input:
# S = "aaaabbaa"
# Output:
# aabbaa
# Explanation:
# The longest palindrome string present in
# the given string is "aabbaa".


def longestPalindrome(self, S):
  max=''
  for j in range(0,len(S)):
      for i in range(j,len(S)):
          a=S[j:i+1]
          if a==a[::-1] and len(max)<len(a):
              max=a
  return max
