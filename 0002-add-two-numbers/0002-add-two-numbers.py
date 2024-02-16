# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(0)
        pointer = ans
        carry = 0
        sum_ = 0
        while l1 or l2 is not None:
            sum_ = carry
            if l1 is not None:
                sum_+=l1.val
                l1 = l1.next
            if l2 is not None:
                sum_+=l2.val
                l2 = l2.next
            carry = int(sum_/10)
            pointer.next = ListNode(sum_%10)
            pointer = pointer.next
        if carry>0:
            pointer.next = ListNode(carry)
        return ans.next
        