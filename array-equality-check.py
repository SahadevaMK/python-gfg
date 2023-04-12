class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        
        #return: True or False
        
        #code here
        b = sorted(A)
        c = sorted(B)
        
        if (b == c):
            return True
        else:
            return False
