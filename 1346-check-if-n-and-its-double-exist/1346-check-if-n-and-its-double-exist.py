class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        seen = set()
        
        for num in arr:
            # 현재 숫자의 2배가 이미 나왔거나
            # 현재 숫자가 짝수이고 그 절반이 이미 나왔다면 조건 충족
            if num * 2 in seen or (num % 2 == 0 and num // 2 in seen):
                return True
            
            # 현재 숫자를 기록
            seen.add(num)
            
        return False