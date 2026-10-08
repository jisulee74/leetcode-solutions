from collections import Counter, defaultdict

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # c1 = Counter(arr)

        # return len(c1.values()) == len(set(c1.values()))
        count_dict = defaultdict(int)

        for num in arr:
            count_dict[num] += 1
        
        return len(count_dict.values()) == len(set(count_dict.values()))