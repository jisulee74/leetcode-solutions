class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m1 = m2 = m3 = None

        for num in nums:
            if num in (m1, m2, m3):
                continue

            if m1 is None or num > m1:
                m3, m2, m1 = m2, m1, num
            elif m2 is None or num > m2:
                m3, m2 = m2, num
            elif m3 is None or num > m3:
                m3 = num

        return m3 if m3 is not None else m1                