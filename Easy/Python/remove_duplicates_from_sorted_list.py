class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return None
        dummy = ListNode(head.val)
        current = dummy
        head = head.next
        
        while head:
            if head.val != current.val:
                current.next = head
                current = current.next
                
            head = head.next
            current.next = None
            
        return dummy
