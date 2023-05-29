#User function Template for python3
class Solution:

	
	def removeDuplicates(self,str):
	    # code here
	    lst = []
	    for i in str:
	        if i not in lst:
	            lst.append(i)
	    serv = ''.join(lst)
	    return serv
