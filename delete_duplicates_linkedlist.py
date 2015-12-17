# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        ptr_1 = A
        ptr_2 = A
        while ptr_2 != None:
            ptr_1 = ptr_1.next
            while ptr_1 and ptr_1.val == ptr_2.val:
                ptr_1 = ptr_1.next
                ptr_2.next = ptr_1
            ptr_2 = ptr_2.next
        return A