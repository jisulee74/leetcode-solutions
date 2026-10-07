from collections import defaultdict

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        count_dict = defaultdict(int)

        for num in arr:
            count_dict[num] += 1
        
        return len(set(count_dict.values())) == len(count_dict.values())