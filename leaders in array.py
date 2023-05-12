class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        #Code here
        ans = []
        maxim = A[N-1]
        for i in range(N-1,-1,-1):
            if A[i]>=maxim:
                maxim=A[i]
                ans.append(maxim)
        ans.reverse()
        return ans
            
