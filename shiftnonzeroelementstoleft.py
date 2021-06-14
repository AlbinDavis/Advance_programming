n=15
arr=[0,0, 0, 0, 0 ,9, 0 ,31, 31 ,0, 0 ,12 ,46, 0, 4]

i=0
j=0
while j<len(arr):
    if arr[j]==0:
        j+=1
    else:
        if i!=j:
            arr[i]=arr[j]
            arr[j]=0
            i+=1
print(arr)
