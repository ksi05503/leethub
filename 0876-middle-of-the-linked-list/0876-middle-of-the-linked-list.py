# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        carry = head
        nodes = []
        
        while carry.next != None:
            nodes.append(carry)
            carry = carry.next
        nodes.append(carry)
            
        return nodes[int((len(nodes))/ 2)]
    
