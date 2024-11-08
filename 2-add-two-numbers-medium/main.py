# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        spare = 0
        result = 0
        while l1 is not None or l2 is not None or spare != 0:
            current = spare
            if l1 is not None:
                current += l1.val
                l1 = l1.next
            if l2 is not None:
                current += l2.val
                l2 = l2.next
            if current >= 10:
                spare = 1
                current = current % 10
            else:
                spare = 0
            
            if result == 0:
                result = ListNode(current, None)
                current_node = result
            else:
                current_node.next = ListNode(current, None)
                current_node = current_node.next
        return result