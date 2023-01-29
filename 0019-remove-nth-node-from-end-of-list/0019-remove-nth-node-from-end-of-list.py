# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """ 
        
        slow = fast = head
        
        for _ in range(n):
            fast = fast.next

        # N번째가 첫번째 노드인 경우
        if fast == None:
            return head.next
         
        while fast.next:
            slow = slow.next
            fast = fast.next
            
        # N번째가 마지막 노드인 경우
        if slow.next == None:
            return None
            
        slow.next = slow.next.next
        
        return head
            
            
            