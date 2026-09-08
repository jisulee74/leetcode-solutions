class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        last_non_zero_found_at = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                # Avoid swapping with itself to optimize performance
                if i != last_non_zero_found_at:
                    nums[last_non_zero_found_at], nums[i] = nums[i], nums[last_non_zero_found_at]
                last_non_zero_found_at += 1