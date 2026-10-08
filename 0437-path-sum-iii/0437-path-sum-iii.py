# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        if not root:
            return 0
            
        # 1. 현재 노드를 시작점으로 하는 경로의 개수 +
        # 2. 왼쪽 자식 노드를 새로운 루트로 하여 다시 시작하는 경우의 개수 +
        # 3. 오른쪽 자식 노드를 새로운 루트로 하여 다시 시작하는 경우의 개수
        return (self.count_paths(root, targetSum) + 
                self.pathSum(root.left, targetSum) + 
                self.pathSum(root.right, targetSum))

    def count_paths(self, node, target):
        """특정 노드에서 출발해 아래로 내려가며 합이 target이 되는 경로를 찾는 도우미 함수"""
        if not node:
            return 0
            
        count = 0
        # 현재 노드의 값이 target과 같다면 경로 1개 추가
        if node.val == target:
            count += 1
            
        # 남은 target 값을 가지고 왼쪽과 오른쪽 자식으로 계속 탐색
        count += self.count_paths(node.left, target - node.val)
        count += self.count_paths(node.right, target - node.val)
        
        return count