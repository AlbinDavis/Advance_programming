
# Given an array A of N length. We need to calculate the next greater element for each element in a given array. If the next greater element is not available in a given array then we need to fill ‘-10000000’ at that index place.

# Example 1:

# â€‹Input : arr[ ] = {13, 6, 7, 12}
# Output : _ 7 12 13 
# Explanation:
# Here, at index 0, 13 is the greatest value 
# in given array and no other array element 
# is greater from 13. So at index 0 we fill 
# '-10000000'.


# â€‹Example 2:

# Input : arr[ ] = {6, 3, 9, 8, 10, 2, 1, 15, 7} 
# Output :  7 6 10 9 15 3 2 _ 8

def greaterElement (arr,  n) : 
        d=set(arr)
        for i in range(n):
            s=arr[i]
            c=False
            while s<=max(d):
                if s+1 in d:
                    arr[i]=s+1
                    c=True
                    break
                s+=1
            if not c:
                arr[i]=-10000000
    
        return arr
