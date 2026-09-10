class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0 
        
        for i, num in enumerate(nums):
            for j in range(len(nums)):
                if i != j:
                    if num < nums[j] * 2:
                        break
                    count += 1
            if count == len(nums) - 1:
                return i
            count = 0
            
        return -1
                    
        