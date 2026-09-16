# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #if no nodes return None
        if head == None:
            return head

        cur = head
        prev = None
        while cur != None:
            temp = cur.next #save address of next node
            cur.next = prev #point curnext to prv
            prev = cur #update prev to cur
            cur = temp #update cur to (cur.next)
        
        head = prev
        return head