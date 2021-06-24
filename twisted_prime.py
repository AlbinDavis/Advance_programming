# Given a number N. Check whether N is a Twisted Prime number or not.
# Note: A number is called Twisted Prime if it is a prime and its reverse is also a prime.

# Example 1:

# Input: N = 97
# Output: 1
# Explanation: 97 is a prime number. Its 
# reverse 79 isalso a prime number. Thus 
# 97 is a  twisted Prime and so, answer is 1.
# Example 2:

# Input: N = 43
# Output: 0
# Explanation: 43 is a prime number but its 
# reverse 34 is not a prime.So, 43 is not a 
# twisted prime and thus, answer is 0.    
  
  
  
  def isTwistedPrime(self,n):
        s=0
        c=n
        while n:
            r=n%10
            n=n//10
            s=s*10+r
            
        def isprime(n):
            f=True
            if n==1 or n==0:
                return False
            for i in range(2,(n//2)+1):
                if n%i==0:
                    f=False
            return f
    
        if isprime(c) and isprime(s):
            return 1
        else:
            return 0
