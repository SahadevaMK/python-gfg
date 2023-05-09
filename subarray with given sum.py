#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s):
        a = []
        currsum=arr[0]
        start = 0
        i=1
        while(i<=n):
            while(currsum>s and start<i-1):
                currsum=currsum-arr[start]
                start+=1
            if(currsum==s):
                a.append(start+1)
                a.append(i)
                return a
            if(i<n):
                currsum = currsum+arr[i]
            i+=1
        a.append(-1)
        return a
