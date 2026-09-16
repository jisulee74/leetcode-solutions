class Solution(object):
    def generate(self, numRows):
        """:type numRows: int :rtype: List[List[int]]"""
        if numRows == 0:
            return []
        
        # 첫 번째 행은 무조건 [1]로 시작합니다.
        triangle = [[1]]
        
        for i in range(1, numRows):
            prev_row = triangle[i - 1]
            current_row = [1]  # 각 행의 시작은 항상 1
            
            # 중간 값 계산 (바로 위 행의 인접한 두 원소의 합)
            for j in range(1, len(prev_row)):
                current_row.append(prev_row[j - 1] + prev_row[j])
                
            current_row.append(1)  # 각 행의 끝은 항상 1
            triangle.append(current_row)
            
        return triangle