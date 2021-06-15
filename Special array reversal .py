# Given a string S, containing special characters and all the alphabets, reverse the string without
# affecting the positions of the special characters.

# Example 1:

# Input: S = "A&B"
# Output: "B&A"
# Explanation: As we ignore '&' and
# then reverse, so answer is "B&A".
# â€‹Example 2:

# Input: S = "A&x#
# Output: "x&A#"
# Explanation: we swap only A and x.
def reverse(self, s):
    l=list(s)
    i=0
    j=len(s)-1
    while i<j:
        if l[i].isalpha()==False:
            i+=1
            continue
        elif l[j].isalpha()==False:
            j-=1
            continue
        else:
            l[i],l[j]=l[j],l[i]
            i+=1
            j-=1

    return ''.join(l)
