class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,a,n,b,m):
        c = a+b
        d = set(c)
        return len(d)
        
        #code here
