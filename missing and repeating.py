class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        ans=[0]*2
        for i in range(n):
            if arr[abs(arr[i])-1] > 0:
                arr[abs(arr[i])-1] = -arr[abs(arr[i])-1]
            else:
                ans[0]=abs(arr[i])
    
        for i in range(n):
            if arr[i]>0:
                ans[1]=i+1
        return ans
