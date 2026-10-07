class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        max_water = 0
        right = len(height) - 1

        while left < right:
            current_width = right - left
            current_height = min(height[left], height[right])
            max_water = max(max_water, current_height * current_width)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water