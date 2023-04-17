class Solution:
    def search(self, A : list, l : int, h : int, key : int):
        l = 0
        h = len(A)-1
        for i in range(len(A)):
            if (A[i] == key):
                return i
        else:
            return -1
            
