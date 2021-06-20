
# Easy Accuracy: 49.96% Submissions: 16699 Points: 2
# Given an array Arr of N positive integers and another number X. Determine whether or not there exist two elements in Arr whose sum is exactly X.

# Example 1:

# Input:
# N = 6, X = 16
# Arr[] = {1, 4, 45, 6, 10, 8}
# Output: Yes
# Explanation: Arr[3] + Arr[4] = 6 + 10 = 16
# Example 2:

# Input:
# N = 5, X = 10
# Arr[] = {1, 2, 4, 3, 6}
# Output: Yes
# Explanation: Arr[2] + Arr[4] = 4 + 6 = 10
s = set()
for i in arr:
    if(x - i in s):
        return "Yes"
    s.add(i)
