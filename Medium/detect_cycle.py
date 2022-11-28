"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
"""

Let F be the distance before the loop starts, a is the distance of the tortoise minus F, b is the distance of the loop minus a
2* distance(tortoise) = =distance(hare)
2(F+a) =F+a+b+a
2F+2a = =F+2a+b
F =b
​"""
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        hare = tortoise = head
        if not head:
            return None
        while hare.next != None and hare.next.next != None:
            hare = hare.next.next
            tortoise = tortoise.next
            if hare == tortoise:
                base = head
                loop_back = tortoise
                while base != loop_back:
                    base = base.next
                    loop_back = loop_back.next
                return base
        return None