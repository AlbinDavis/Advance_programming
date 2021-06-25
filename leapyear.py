def isLeap (self, N):
    if N%400 is 0:
        return 1
    elif N%100 is 0:
        return 0
    elif N%4 is 0:
        return 1
    else:
        return 0
