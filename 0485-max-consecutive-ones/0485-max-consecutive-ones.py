class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one_count = 0
        max_count = 0
        
        for num in nums:
            if num == 1:
                one_count += 1 
                if one_count > max_count:
                    max_count = one_count
            else:
                one_count = 0
                
        return max_count
        

            
            