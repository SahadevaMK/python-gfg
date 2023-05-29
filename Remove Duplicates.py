class Solution:
	def removeDups(self, S):
		# code here
		lst = []
		for i in S:
		    if i not in lst:
		        lst.append(i)
		servo = ''.join(lst)
		return servo
