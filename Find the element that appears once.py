# Given a sorted array A[] of N positive integers having all the numbers occurring exactly twice, except for one number which will occur only once. Find the number occurring only once.

# Example 1:

# Input:
# N = 5
# A = {1, 1, 2, 5, 5}
# Output: 2
# Explanation: 
# Since 2 occurs once, while
# other numbers occur twice, 
# 2 is the answer.
# Example 2:

# Input:
# N = 7
# A = {2, 2, 5, 5, 20, 30, 30}
# Output: 20
# Explanation:
# Since 20 occurs once, while
# other numbers occur twice, 
# 20 is the answer.

  def search(self, a, n):
      for i in range(0,len(a)-1,2):
          if a[i+1]!=a[i]:
              return a[i]
      return a[len(a)-1]
