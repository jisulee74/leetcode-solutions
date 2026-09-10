class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num_str = "".join(map(str, digits))
        plus_one = int(num_str) + 1
        
        return [int(char) for char in str(plus_one)]