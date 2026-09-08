class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        last_non_zero_found_at = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                # 자기 자신과의 교환을 피하기 위해 인덱스가 다를 때만 스왑
                if i != last_non_zero_found_at:
                    nums[last_non_zero_found_at], nums[i] = nums[i], nums[last_non_zero_found_at]
                last_non_zero_found_at += 1