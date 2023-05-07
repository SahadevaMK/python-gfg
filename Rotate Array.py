
class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self,A,D,N):
        for j in range(D):
            temp=A[0]
            for i in range(N-1):
                A[i]=A[i+1]
            A[N-1]=temp
      
