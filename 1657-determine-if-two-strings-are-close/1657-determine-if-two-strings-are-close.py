from collections import defaultdict
class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if len(word1) != len(word2):
            return False
        # countdict1 = defaultdict(int)
        # countdict2 = defaultdict(int)

        # for word in word1:
        #     countdict1[word] += 1
        
        # for word in word2:
        #     countdict2[word] += 1

        c1 = Counter(word1)
        c2 = Counter(word2)

        # return sorted(countdict1) == sorted(countdict2) and sorted(countdict1.values()) == sorted(countdict2.values())

        return set(c1) == set(c2) and sorted(c1.values()) == sorted(c2.values())
