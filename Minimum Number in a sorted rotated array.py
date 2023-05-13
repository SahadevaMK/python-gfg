class Solution:
    
    #Function to find the minimum element in sorted and rotated array.
    def minNumber(self, arr,low,high):
        #Your code here
        min = arr[0]
        
        for i in range(0,len(arr)):
            if arr[i]<min:
                min = arr[i]
        return min
