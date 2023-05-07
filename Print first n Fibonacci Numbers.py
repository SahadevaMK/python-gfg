#User function Template for python3

class Solution:
    #Function to return list containing first n fibonacci numbers.
    def printFibb(self,n):
        # your code here
        fib = []
        n1 = 0
        n2 = 1
        # fib.append(n1)
        fib.append(n2)
        for i in range(0,n-1):
            n3 = n1+n2
            n1 = n2
            n2 = n3
            fib.append(n3)
        return fib
