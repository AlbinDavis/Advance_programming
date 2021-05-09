li=[1,2,3,-2,5]
def maxSubArraySum(a):
    s = 0
    r = 0
    for i in a:
        if s + i < 0:
            s = 0
        else:
            s += i
        r = max(r, s)
    return r
print(maxSubArraySum(li))