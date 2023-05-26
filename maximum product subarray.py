class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr, n):
		# code here
		minval = arr[0]
		maxval = arr[0]
		maxproduct = arr[0]
		for i in range(1,n,1):
		    if (arr[i]<0):
		        temp = maxval
		        maxval = minval
		        minval = temp
		    maxval= max(arr[i],maxval*arr[i])
		    minval = min(arr[i],minval*arr[i])
		    
		    maxproduct = max(maxproduct,maxval)
		return maxproduct
