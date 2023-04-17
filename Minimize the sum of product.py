class Solution:
    def minValue(self, a, b, n):
        # Your code goes here
        ans = 0
        a.sort()
        b.sort(reverse = True)
        for i in range(len(a)):
            ans=ans+a[i]*b[i]
        return ans
            
                
        
