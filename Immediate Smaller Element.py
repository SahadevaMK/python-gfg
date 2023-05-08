#User function Template for python3
class Solution:

	def immediateSmaller(self,arr,n):
		# code here
		A=[]
# 		arr[n-1] = -1
		for i in range(n-1):
		    if (arr[i]>arr[i+1]):
		        arr[i]=arr[i+1]
		    else:
		        arr[i]=-1
		arr[n-1]=-1
		return arr
		
