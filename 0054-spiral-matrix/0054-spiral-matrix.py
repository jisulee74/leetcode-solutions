class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(matrix), len(matrix[0])
        result = []
        row, col = 0, 0
        direction = 1
        m_end_updated, n_end_updated = m, n
        m_start_updated, n_start_updated = 0, 0
        
        while len(result) < m * n:
            result.append(matrix[row][col])
            
            if direction == 1:
                if col == n_end_updated - 1:
                    row += 1
                    m_start_updated += 1
                    direction = 2                
                else:
                    col += 1
            elif direction == 2:
                if row == m_end_updated - 1:
                    col -= 1
                    n_end_updated -= 1
                    direction = 3
                else:
                    row += 1
            elif direction == 3:
                if col == n_start_updated:
                    row -= 1
                    m_end_updated -= 1
                    direction = 4
                else:
                    col -= 1
            else:
                if row == m_start_updated:
                    col += 1
                    n_start_updated += 1
                    direction = 1
                else:
                    row -= 1
        return result