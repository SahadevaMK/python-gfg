class Solution:	
	def binarysearch(self, arr, n, k):
	    
		# code here
		l=0
		u=n-1
		while (l<=u):
		    mid = (l+u)//2
		    if arr[mid]==k:
		        return mid
		    elif arr[mid]<k:
		        l = mid+1
		    else:
		        u=mid-1
	    return -1
