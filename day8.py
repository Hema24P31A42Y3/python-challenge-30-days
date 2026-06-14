class Solution(object):
    def findNonMinOrMax(self, nums):
        mn = min(nums)
        mx = max(nums)
        for i in nums:
            if i != mn and i != mx:
                return i
        return -1

        
