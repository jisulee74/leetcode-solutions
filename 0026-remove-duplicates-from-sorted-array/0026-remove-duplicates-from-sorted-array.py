class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 0 if len(nums) != 1 else 1
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[index] = nums[i]
                index += 1
            if i == len(nums)-2:
                nums[index] = nums[i+1]
                index += 1
        
        return index
