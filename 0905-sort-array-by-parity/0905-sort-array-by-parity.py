class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        last_odd_found_at = 0
        
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                if i != last_odd_found_at:
                    nums[last_odd_found_at], nums[i] = nums[i], nums[last_odd_found_at]
                last_odd_found_at += 1
                
        return nums