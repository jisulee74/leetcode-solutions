class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        
        if digits[0] == 9 and n == 1:
            digits[0] = 0
            digits.insert(0, 1)
        else:
            if digits[n-1] != 9:
                digits[n-1] += 1
            else:
                digits[n-1] = 0

                for i in range(n-2, 0, -1):
                    if digits[i] == 9:
                        digits[i] = 0
                    else:
                        digits[i] += 1
                        return digits
                        
                if digits[0] == 9:
                    digits[0] = 0
                    digits.insert(0, 1)
                else:
                    digits[0] += 1


        return digits