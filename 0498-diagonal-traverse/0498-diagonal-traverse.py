class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(mat), len(mat[0])
        from collections import defaultdict

        diagonals = defaultdict(list)

        for i in range(m):
            for j in range(n):
                diagonals[i+j].append(mat[i][j])

        result = []

        for d in range(m + n - 1):
            if d % 2 == 0:
                result.extend(diagonals[d][::-1])
            else:
                result.extend(diagonals[d])
        
        return result