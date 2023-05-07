class Solution:
    ##Complete this function
    def searchInSorted(self,arr, N, K):
        #Your code here
        for i in range(len(arr)):
            if (arr[i]==K):
                return 1
        return -1
