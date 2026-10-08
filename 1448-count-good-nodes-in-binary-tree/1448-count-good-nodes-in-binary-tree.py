# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 내부 재귀 함수를 이용해 현재까지의 최댓값(max_so_far)을 함께 전달합니다.
        def dfs(node, max_so_far):
            if not node:
                return 0
            
            # 1. 현재 노드가 굿 노드인지 확인 (지금까지의 최댓값보다 크거나 같다면 굿 노드)
            count = 1 if node.val >= max_so_far else 0
            
            # 2. 내려갈 때의 최댓값을 현재 노드 값과 비교해서 더 큰 값으로 갱신
            new_max = max(max_so_far, node.val)
            
            # 3. 왼쪽과 오른쪽 자식으로 넘어가면서 굿 노드 개수를 누적해서 더함
            count += dfs(node.left, new_max)
            count += dfs(node.right, new_max)
            
            return count

        # 루트 노드의 값으로 시작하며, 루트는 항상 경로의 최댓값이므로 굿 노드입니다.
        return dfs(root, root.val)