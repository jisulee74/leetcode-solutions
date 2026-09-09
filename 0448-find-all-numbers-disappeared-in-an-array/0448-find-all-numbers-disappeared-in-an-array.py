class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]

        return [i+1 for i, num in enumerate(nums) if num > 0]