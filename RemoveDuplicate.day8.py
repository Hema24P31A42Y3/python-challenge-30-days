class Solution(object):
    def removeDuplicate(self, nums):
        result = []

        for i in range(len(nums)):
            if nums[i] not in result:
                result.append(nums[i])

        return result
