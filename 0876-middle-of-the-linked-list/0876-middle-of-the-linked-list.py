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
        slow = fast = head
        
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            
            
        return slow
        
        
''' 어레이에 때려넣고 길이 구해서 찾는 쉬운 방법 (두 방법 모두 시간복잡도는 O(n))
        carry = head
        nodes = []
        
        while carry.next != None:
            nodes.append(carry)
            carry = carry.next
        nodes.append(carry)
            
        return nodes[int((len(nodes))/ 2)]
'''
        
        
        