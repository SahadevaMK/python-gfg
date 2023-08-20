class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = {}
        arr2 = []
        for i in nums:
            if i in res:
                res[i]+=1
            else:
                res[i]=1
        # n= len(nums)
        threshold = len(nums) // 3
        for i in res:
            if res[i]>threshold:
                arr2.append(i)
        return arr2
