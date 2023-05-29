class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self,a,b):
        #code here
        first = sorted(a)
        second = sorted(b)
        if (first == second):
            return True
        else:
            return False
            

