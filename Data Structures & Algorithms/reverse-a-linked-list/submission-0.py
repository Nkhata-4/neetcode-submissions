# Definition for singly-linked list.
'''class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next'''

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        
        stack = [head.val]
        temp = head
        while temp.next:
            temp = temp.next
            stack.append(temp.val)
        
        temp = head
        while temp.next:
            temp.val = stack.pop()
            temp = temp.next
        
        temp.val = stack.pop()
        return head
        
        
        
        
        
        
        
        