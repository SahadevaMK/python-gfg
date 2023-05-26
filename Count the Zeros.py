class Solution:
    def countZeroes(self, arr, n):
        # code here
        c=0
        for i in range(0,n,1):
            if arr[i]==0: c+=1
        return c
                
