# Given a sorted array of positive integers. Your task is to rearrange  the array elements alternatively i.e first element should be max value, second should be min value, third should be second max, fourth should be second min and so on.

# Example 1:

# Input:
# N = 6
# arr[] = {1,2,3,4,5,6}
# Output: 6 1 5 2 4 3
# Explanation: Max element = 6, min = 1, 
# second max = 5, second min = 2, and 
# so on... Modified array is : 6 1 5 2 4 3.
# Example 2:

# Input:
# N = 11
# arr[]={10,20,30,40,50,60,70,80,90,100,110}
# Output:110 10 100 20 90 30 80 40 70 50 60
# Explanation: Max element = 110, min = 10, 
# second max = 100, second min = 20, and 
# so on... Modified array is : 
# 110 10 100 20 90 30 80 40 70 50 60.



#User function Template for python3

class Solution:
    #Complete this function
    # Function to rearrange  the array elements alternately.
    def rearrange(self,arr, n):
        maxi=n-1
        mini=0
        me=arr[maxi]+1
        for i in range(n):
            if i%2==0:
                arr[i]+=arr[maxi]%me*me
                maxi-=1
            else:
                 arr[i]+=arr[mini]%me*me
                 mini+=1
        for i in range(n):
            arr[i]//=me
            
        
        
    #     a=arr.copy()
    #     u=n-1
    #     l=0
    #     for i in range(n):
    #         if i%2==0:
    #             arr[i]=a[u]
    #             u-=1
    #         else:
    #             arr[i]=a[l]
    #             l+=1
