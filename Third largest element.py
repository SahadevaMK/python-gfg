class Solution:
    def thirdLargest(self,a, n):
        # code here
        a.sort()
        return a[-3]
