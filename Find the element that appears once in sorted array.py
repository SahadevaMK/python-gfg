class Solution:
    def findOnce(self,arr : list, n : int):
        # Complete this function
        ans = 0
        for i in range(len(arr)):
            ans = ans^arr[i]
        return ans
