# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # 노드가 1개인 경우
        if not head or not head.next:
            return None
        
        # 느린 포인터는 한 칸씩, 빠른 포인터는 두 칸 씩 이동
        slow = head
        fast = head.next.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slow가 가리키는 노드의 다음 노드(중간 노드)를 건너뛰어 삭제
        slow.next = slow.next.next

        return head