class Solution:
    def findMin(self, arr, n):
        #complete the function here
        min=arr[0]
        for i in range(1,n,1):
            if (arr[i]<min):
                min = arr[i]
        return min
