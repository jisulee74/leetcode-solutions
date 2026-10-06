from collections import defaultdict, Counter

class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if len(word1) != len(word2):
            return False
        
        # 알파벳별 count 의 개수 및 종류가 같으면 true
        count_dict_1 = defaultdict(int)
        count_dict_2 = defaultdict(int)

        for char in word1:
            count_dict_1[char] += 1
        
        for char in word2:
            count_dict_2[char] += 1

        return Counter(list(count_dict_1.values())) == Counter(list(count_dict_2.values())) and Counter(list(count_dict_1)) == Counter(list(count_dict_2))

        