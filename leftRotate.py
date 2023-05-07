def leftrotate(arr,n):
    temp = arr[0]
    for i in range(n-1,0,-1):
        arr[i]=arr[i+1]
    arr[n-1] = temp;
a = [1,2,3,4,5]
leftrotate(a,5)
print(a)   
