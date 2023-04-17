class Solution:

	def print2largest(self,arr, n):
        len(set(arr))<2:
            return -1
		return sorted(set(arr))[-2]
