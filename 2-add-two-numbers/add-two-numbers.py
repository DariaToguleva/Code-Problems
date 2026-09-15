# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        final = ListNode()
        dummy = final
        carry = 0

        while l1 or l2 or carry:
            if not l1:
                i = 0
            else:
                i = l1.val
                l1 = l1.next    
            if not l2:
                j = 0   
            else:
                j = l2.val
                l2 = l2.next    
            sumi = i + j + carry
            carry = sumi // 10
            spot = sumi % 10

            dummy.next = ListNode(spot)
            dummy = dummy.next
 
        return final.next        



