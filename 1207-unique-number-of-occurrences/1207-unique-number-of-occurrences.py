from collections import Counter

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        c1 = Counter(arr)

        return len(c1.values()) == len(set(c1.values()))