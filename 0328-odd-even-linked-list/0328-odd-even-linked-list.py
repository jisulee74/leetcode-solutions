# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # 노드가 없거나 1개/2개 뿐이면 그대로 반환
        if not head or not head.next:
            return head
        
        #odd는 홀 수 번째 노드들의 체인, even은 짝수 번째 노드들의 체인
        odd = head
        even = head.next

        # 나중에 홀수 그룹의 끝과 짝수 그룹의 시작을 이어주기 위해 짝수 그룹의 헤드 기억
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        # 홀수 그룹의 끝과 짝수 그룹의 시작점 연결
        odd.next = even_head

        return head