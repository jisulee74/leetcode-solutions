class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left_product = 1
        answer = [1] * len(nums)

        for i, num in enumerate(nums):
            answer[i] = left_product
            left_product *= num
        
        right_product = 1
        for i in range(len(nums)-1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]

        return answer
