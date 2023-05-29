class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        # code here
        sentence = S.split('.')
        names = sentence[-1::-1]
        final = '.'.join(names)
        return final

