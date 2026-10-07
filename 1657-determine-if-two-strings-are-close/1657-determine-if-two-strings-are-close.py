from collections import defaultdict
class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        countdict1 = defaultdict(int)
        countdict2 = defaultdict(int)

        for word in word1:
            countdict1[word] += 1
        
        for word in word2:
            countdict2[word] += 1

        return sorted(countdict1) == sorted(countdict2) and sorted(countdict1.values()) == sorted(countdict2.values())