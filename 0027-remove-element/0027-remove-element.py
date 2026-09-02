class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # for i in range(0, len(nums)):
        #     if nums[i] == val:
        #         nums[i] = nums[i+1]
        nums[:] = [x for x in nums if x != val]
        
        return len(nums)