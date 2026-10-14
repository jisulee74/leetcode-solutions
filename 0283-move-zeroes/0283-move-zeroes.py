class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        last_zero_found_at = 0

        # for i, num in enumerate(nums):
        #     if num != 0:
        #         if i != last_zero_found_at:
        #             num, nums[last_zero_found_at] = nums[last_zero_found_at], num
        #         last_zero_found_at += 1
        
        for i in range(len(nums)):
            if nums[i] != 0:
                if i != last_zero_found_at:
                    nums[i], nums[last_zero_found_at] = nums[last_zero_found_at], nums[i]
                last_zero_found_at += 1
                