# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        for _ in range(n):
            fast = fast.next
        if fast == None:
            return head.next
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head
#  TC = O(N)  , SC = O(1)


        # if head is None:
        #     return None
        # length = 0
        # temp = head
        # while temp != None:
        #     length += 1
        #     temp = temp.next
        # if length == n:
        #     new_head =  head.next
        #     del head   # or  head = None
        #     return new_head
        # position_to_stop = length - n
        # temp = head
        # count = 1
        # while count < position_to_stop:
        #     temp = temp.next
        #     count += 1
        # temp.next = temp.next.next
        # return head
        # #  TC = O(2N) - O(N),  SC = O(1)



'''
19. Remove Nth Node From End of List
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 

Follow up: Could you do this in one pass?

'''
