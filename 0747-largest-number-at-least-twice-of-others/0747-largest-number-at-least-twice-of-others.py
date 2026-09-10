class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = max2 = -1
        index = -1

        for i, num in enumerate(nums):
            if num > max1:
                max2, max1 = max1, num
                index = i
            elif num > max2:
                max2 = num
        
        return index if max1 >= max2 * 2 else -1
                    
        