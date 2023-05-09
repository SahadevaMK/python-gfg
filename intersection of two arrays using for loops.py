#User function Template for python3

#Function to return the count of the number of elements in
#the intersection of two arrays.
class Solution:
    def NumberofElementsInIntersection(self,a, b, n, m):
        #return: expected length of the intersection array.
        #code here
        c=[]
        for i in range(0,n):
            for j in range(0,m):
                if (a[i]==b[j]):
                    c.append(a[i])
        d = len(c)
        return d
