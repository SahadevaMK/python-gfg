class Solution:
    def NumberofElementsInIntersection(self,a, b, n, m):
        #return: expected length of the intersection array.
        #code here
        hs = set()
        c=0
        for i in range(0,n):
            hs.add(a[i])
        for j in range(0,m):
            if b[j] in hs:
                c+=1
                hs.remove(b[j])
        return c
      
