class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # 원래 배열을 복사하여 정렬된 기대 배열(expected)을 만듭니다.
        expected = sorted(heights)
        
        # 두 배열의 원소를 비교하여 서로 다른 값의 개수를 셉니다.
        count = 0
        for h, e in zip(heights, expected):
            if h != e:
                count += 1
                
        return count