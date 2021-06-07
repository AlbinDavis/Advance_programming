l=[1,1,1,0,1]

for i in range(len(l)):
    p1=sum(l[:i])-l[:i].count(0)
    p2=sum(l[i:])-l[i:].count(0)
    if p1>p2:
        print(i)
        break