class Solution:
     
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr, n):
         
        
        shift = self.segregate(arr, n)
         
       
        return self.findMissingPositive(arr[shift:], n - shift)
        
   
    def segregate(self,arr, n):
        j = 0
        for i in range(n):
            
            if (arr[i] <= 0):
               
                arr[i], arr[j] = arr[j], arr[i]
                
                j += 1
                
        return j
        
   
    def findMissingPositive(self,arr, n):
         
       
        for i in range(n):
            if (abs(arr[i]) - 1 < n and arr[abs(arr[i]) - 1] > 0):
                arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1]
                 
        
        for i in range(n):
            
            if (arr[i] > 0):
                #returning the first index where value is positive.
                # 1 is added because indexing starts from 0.
                return i + 1
                
        return n+1
        
        
        
