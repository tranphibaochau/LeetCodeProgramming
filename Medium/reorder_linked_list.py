# LeetCode problem # 143: https://leetcode.com/problems/reorder-list/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorder_list(head):
    """
    reorder the linked list in-place.
    :type head: ListNode
    """
    # find the middle and the end node in the linked list
    mid = end = head
    prev = None
    while end and end.next:
        mid = mid.next
        end = end.next
        prev = end
        end = end.next
    # if end node jumped too far, go back one node
    if not end:
        end = prev

    # reverse linked list from the middle node to the end node
    # start by making sure middle node points to None
    prev = None
    node = mid
    while node:
        temp = node.next
        node.next = prev
        prev = node
        node = temp

    # reorder the nodes, making sure to end the loop if end node or head node reaches the middle
    while end != mid and head != mid:
        temp_head = head.next
        temp_end = end.next
        head.next = end
        end.next = temp_head
        head = temp_head
        end = temp_end
