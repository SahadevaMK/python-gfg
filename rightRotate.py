def rightrotate(arr,n):
    temp = arr[n-1]
    for i in range(n-1,0,-1):
        arr[i]=arr[i-1]
    arr[0] = temp;
a = [1,2,3,4,5]
rightrotate(a,5)
print(a)   
