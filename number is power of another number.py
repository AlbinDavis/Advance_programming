
# Given two positive numbers X and Y, check if Y is a power of X or not.

 

# Example 1:

# Input:
# X = 2, Y = 8
# Output:
# 1
# Explanation:
# 23 is equal to 8.
 

# Example 2:

# Input:
# X = 1, Y = 3
# Output:
# 0
# Explanation:
# Any power of 1 is not 
# equal to 8.

    def isPowerOfAnother (x,y):
        if X==1:
            if Y==1:
                return 1
            else:
                return 0
        
        res1 = math.log(y) // math.log(x);
     
        # Note : this is double
        res2 = math.log(y) / math.log(x);
        
        # compare to the result1 or
        # result2 both are equal
        return 1 if(res1 == res2) else 0;
      
      or
 
        # if X==1:
        #     if Y==1:
        #         return 1
        #     else:
        #         return 0
                

        # p=1
        # while p<Y:
        #     p=p*X
        # if p==Y:
        #     return 1
        # else:
        #     return 0
            
