arr = [1,0,2,4,0,8,0,7]
j=0
arr2=[]
for i in arr:
    if i>0:
        arr2.append(i)
    else:
        j+=1
for i in range(j):
    arr2.append(0)
for k in arr2:
    print(k,end=' ')
