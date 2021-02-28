/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public var val: Int
 *     public var next: ListNode?
 *     public init() { self.val = 0; self.next = nil; }
 *     public init(_ val: Int) { self.val = val; self.next = nil; }
 *     public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }
 * }
 */
class Solution {
    func mergeTwoLists(_ l1: ListNode?, _ l2: ListNode?) -> ListNode? {
        let dummy = ListNode()
        var current = dummy
        
        var newL1 = l1
        var newL2 = l2
        
        while let a = newL1, let b = newL2 {
            if a.val < b.val {
                current.next = a
                newL1 = a.next
            } else {
                current.next = b
                newL2 = b.next
            }
            
            current = current.next!
        }
        
        current.next = newL1 ?? newL2
        
        return dummy.next
    }
}
