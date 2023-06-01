#User function Template for python3

class Solution:
	def AlternatingaMaxLength(self, nums):
		# Code here
		inc = 1
        dec = 1
        n = len(nums)
        # Iterate from second element
        for i in range(1,n):
          
            if (nums[i] > nums[i-1]):
              
                # "inc" changes iff "dec" 
                # changes
                inc = dec + 1
            elif (nums[i] < nums[i-1]):
              
                # "dec" changes iff "inc" 
                # changes
                dec = inc + 1
                
        # Return the maximum length
        return max(inc, dec)
