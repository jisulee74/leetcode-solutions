class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # Create an expected array by copying and sorting the original heights array.
        expected = sorted(heights)
        
        # Compare elements of both arrays and count the mismatches.
        count = 0
        for h, e in zip(heights, expected):
            if h != e:
                count += 1
                
        return count