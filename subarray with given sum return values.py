class Solution:
    def subArraySum(self,arr, n, s):
        arr11=[-1]
        result=[]
        for i in range(1,n+1):
            result.append(arr[i])
            while(sum(result)>s):
                result.pop(0)
            if(sum(result)==s):
                return result
                    
                
        return [-1]
