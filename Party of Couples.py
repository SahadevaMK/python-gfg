class Solution:
    def findSingle(self, N, arr):
        # code here
        ans = 0
        for i in range(len(arr)):
            ans = ans^arr[i]
        return ans
