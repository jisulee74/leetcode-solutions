class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_nums = sorted(set(nums), reverse=True)
        
        if len(sorted_nums) < 3:
            return sorted_nums[0]
        else:
            return sorted_nums[2]