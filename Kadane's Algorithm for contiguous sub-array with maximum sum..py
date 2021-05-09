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
li=[-2, -3, 4, -1, -2, 1, 5, -3]
print(maxSubArraySum(li))