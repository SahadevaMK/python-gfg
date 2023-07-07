import sys
arr1 = [1,3,5,7]
arr2 = [0,2,6,8,9]

n=len(arr1)
m=len(arr2)
arr3 = [0] *(n+m)
i = 0
j = 0
k = 0

while(i<n and j<m):
    if (arr1[i] <= arr2[j]):
        arr3[k] = arr1[i]
        k+=1
        i+=1
    else:
        arr3[k] = arr2[j]
        j+=1
        k+=1

while(i<n):
    arr3[k]=arr1[i]
    i+=1
    k+=1
while(j<m):
    arr3[k]=arr2[j]
    j+=1
    k+=1
print(arr3)

for t in range(m+n):
    if t<n:
        arr1[t] = arr3[t]
    else:
        arr2[t-n] = arr3[t]

print(-sys.maxsize-1)



