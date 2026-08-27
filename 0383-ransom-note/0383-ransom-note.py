from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):

        ran_count = Counter(ransomNote)
        mag_count = Counter(magazine)

        for char, count in ran_count.items():
            if mag_count[char] < count:
                return False

        return True
