# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # 1. Base Case: 노드가 비어있다면(None) 깊이는 0입니다.
        if not root:
            return 0
            
        # 2. 왼쪽 자식 서브트리의 최대 깊이를 재귀적으로 구합니다.
        left_depth = self.maxDepth(root.left)
        
        # 3. 오른쪽 자식 서브트리의 최대 깊이를 재귀적으로 구합니다.
        right_depth = self.maxDepth(root.right)
        
        # 4. 둘 중 더 큰 값에 현재 노드 자신(+1)을 더해 반환합니다.
        return max(left_depth, right_depth) + 1