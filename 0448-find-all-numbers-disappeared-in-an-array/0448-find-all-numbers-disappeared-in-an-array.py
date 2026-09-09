class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        char = {i:0 for i in range(1, n+1)}
        target_value = 0
        
        for num in nums:
            if char[num] != 0:
                char[num] += 1
            else:
                char[num] = 1
                
        return [key for key, value in char.items() if value == target_value]
        