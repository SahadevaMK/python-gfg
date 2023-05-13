class Solution:
    def reArrange(self, arr, N):
        # code here
        oddInd = 1
        evenInd = 0
        while (True): 
              
            while (evenInd < N and arr[evenInd] % 2 == 0): 
                evenInd += 2
                   
            while (oddInd < N and arr[oddInd] % 2 == 1): 
                oddInd += 2
                   
            if (evenInd < N and oddInd < N): 
                    arr[evenInd],arr[oddInd] = arr[oddInd],arr[evenInd]
                   
            else: 
                break
