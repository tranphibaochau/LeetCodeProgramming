##########################################################################################################################################
# Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. 
# The linked list holds the binary representation of a number.
# Return the decimal value of the number in the linked list.
# Input: head = [1,0,1]
# Output: 5
##########################################################################################################################################


def getDecimalValue(self, head: ListNode) -> int:
	#intuition: as we read from left to right, the previous numbers are doubled (so their sum is doubled)
    answer = 0
    while head: 
        answer = 2*answer + head.val 
        head = head.next 
    return answer 