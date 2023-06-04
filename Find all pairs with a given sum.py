class Solution:
    def allPairs(self, A, B, N, M, X):
        li = []
        # Your code goes here 
        for i in range(len(A)):
            for j in range(len(B)):
                if (A[i]+B[j]) == X:
                    li.append((A[i],B[j]))
        return sorted(li)
# thank you