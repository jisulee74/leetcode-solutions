class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left_sum = [0] * len(nums)
        right_sum = [0] * len(nums)

        for i in range(1, len(nums)):
            left_sum[i] = sum(nums[:i])
        
        for i in range(len(nums)-2, -1, -1):
            right_sum[i] = sum(nums[len(nums)-1:i:-1])
        
        for x in range(len(nums)):
            if left_sum[x] == right_sum[x]:
                return x
            else:
                continue

        return -1
        
