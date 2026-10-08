class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        current_sum = sum(nums[:k])
        current_max = current_sum

        for i in range(k, len(nums)):
            current_sum = current_sum - nums[i-k] + nums[i]
            current_max = max(current_max, current_sum)

        return current_max / float(k)