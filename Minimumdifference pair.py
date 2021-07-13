# Given an unsorted array, find the minimum difference between any pair in given array.
 

# Example 1:

# Input: nums = [2, 4, 5, 9, 7]
# Output: 1
# Explanation: Difference between 5 and 4 is 1.
# Example 2:

# Input: nums = [3, 10, 8, 6]
# Output: 2
# Explanation: Difference between 8 and 6 is 2.

def minimum_difference(self, n):
	    n.sort()
	    m=abs(n[0]-n[1])
		for i in range(len(n)-1):
	        if abs(n[i]-n[i+1])<m:
	            m=abs(n[i]-n[i+1])
	    return m  
