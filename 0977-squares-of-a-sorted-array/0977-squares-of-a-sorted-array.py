class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)
        result = [0] * n
        left, right = 0, n-1
        position = n-1

        while left <= right:
            left_val = nums[left] ** 2
            right_val = nums[right] ** 2

            if left_val > right_val:
                result[position] = left_val
                left += 1
            else:
                result[position] = right_val
                right -= 1
            position -= 1
        
        return result

                    
        