# Given a string str and an integer K, find whether the string can be changed into a pangram after at most k operations. A pangram is a sentence containing every letter in the english alphabet. A single operation can be used to swap an existing alphabetic character with any other alphabetic character.


# Example 1:

# Input:
# str = "the quick brown fox jumps over the lazy dog"
# k = 0
# Output: 1
# Explanation: the sentence contains all 26 characters 
# and is already a pangram. 
# Example 2:

# Input:
# str = "aaaaaaaaaaaaaaaaaaaaaaaaaa"
# k = 25
# Output: 1
# Explanation: The word contains 26 instances of 'a'.
# Since only 25 operations are allowed. We can keep
# 1 instance and change all others to make str a pangram.

def kPangram(s1, k):

    s=Counter(s1)
    if abs(len(s1)-s[' '])<26:
        return None
    else:
        
        count=len(s)
        if " " in s:
            count=len(s)-1
        if count==26:
            return 1
        elif k+count>=26:
            return 1
        else:
            return None
