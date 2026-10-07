# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        current = head # 방향을 바꿔야 할 현재 노드

        while current:
            # 1. 다음 노드를 미리 임시 저장
            next_node = current.next
            # 2. 현재 노드의 화살표 방향을 반대(이전 노드)로 뒤집음
            current.next = prev
            # 2. prev와 current를 한 칸식 전진
            prev =  current
            current = next_node

        return prev