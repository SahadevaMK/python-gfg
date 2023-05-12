#User function Template for python3

class Solution:
    def getPairsCount(self, arr, n, k):
        # code here
        count = 0
        for i in range(0,n):
            for j in range(i+1,n):
                if arr[i]+arr[j]==k:
                    count+=1
        return count
