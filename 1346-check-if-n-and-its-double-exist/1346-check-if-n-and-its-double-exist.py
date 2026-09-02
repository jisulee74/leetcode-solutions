class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        count = 0
        
        for i in range(0, len(arr)):
            for j in range(0, len(arr)):
                if arr[i] == 2 * arr[j] and i != j:
                    count += 1
                    break
        
        return True if count != 0 else False