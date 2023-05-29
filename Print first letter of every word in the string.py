class Solution:
	def firstAlphabet(self, S):
		# code here
		lst = []
		first = S.split(' ')
		for i in first:
		    lst.append(i[0])
	    ser = ''.join(lst)
	    return ser
