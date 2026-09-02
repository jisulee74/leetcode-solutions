class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        count = 0
        break_all = False
        
        for i in range(0, len(arr)):
            for j in range(0, len(arr)):
                if arr[i] == 2 * arr[j] and i != j:
                    count += 1
                    break_all = True
                    break
            if break_all:
                break
        
        return True if count != 0 else False