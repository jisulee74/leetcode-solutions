from collections import Counter

class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if len(word1) != len(word2):
            return False
        
        c1 = Counter(word1)
        c2 = Counter(word2)

        # 1. 알파벳 종류가 같고
        # 2. 각 빈도수의 구성이 일치하는지 
        return set(c1.keys()) == set(c2.keys()) and sorted(c1.values()) == sorted(c2.values())
        return set(c1) == set(c2) and sorted(c1.values()) == sorted(c2.values())