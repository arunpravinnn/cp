# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        array = []
        current = head
        while current:
            array.append(current.val)
            current = current.next
        
        array.reverse()

        current = head
        for i in range(len(array)):
            x = current.next
            current.next = ListNode(array[i])
            current.next.next = x
            current = x
        
        current = head
        for i in range(len(array)-1):
            current=current.next
        
        current.next = None

        
        