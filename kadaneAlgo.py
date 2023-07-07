arr = [1,2,3,-2,5]
lmax = arr[0]
gmax = arr[0]
N = len(arr)
for i in range(1,N):
    if (arr[i] > (arr[i]+lmax)):
        lmax = arr[i]
    else:
        lmax = lmax +arr[i]
        gmax = max(gmax,lmax)

print(gmax)

another soln

import sys
class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        ##Your code here
        maxi = -sys.maxsize-1 # maximum sum
        sum = 0
        for i in range(N):
            sum =sum+ arr[i]
            if sum > maxi:
                maxi = sum
            if sum < 0:
                sum = 0
        return maxi
