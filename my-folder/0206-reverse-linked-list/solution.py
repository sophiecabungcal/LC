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
        prev_node = None # prev node processed
        current_node = head # curr node being processed

        while current_node:
            next_node = current_node.next
            
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node

        return prev_node
