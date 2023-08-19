class Solution:

	def count(self,arr, n, x):
		# code here
		result = {}
		for i in arr:
		    if i in result:
		        result[i]+=1
		    else:
		        result[i]=1
	    for j in result:
	        if j == x:
	            return result[j]
	    return 0
