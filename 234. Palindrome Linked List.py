

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def isPalindrome(self, head):
        """
        type head: ListNode
        rtype: bool
        """
        slow = fast = head
        left = []

        while fast and fast.next:
            left.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        
        if fast:
            slow = slow.next

        while slow:
            leftVal = left.pop()
            if leftVal != slow.val:
                return False
            slow = slow.next

        return True

    # Time complexity: O(n)
    # reverse the second half and then compare
    def isPalindrome_sol2(self, head):
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
        
        while node:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True
            
            
            
            