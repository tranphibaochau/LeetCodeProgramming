class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        curr = self.head
        i = 0
        while curr.next and i < index:
            curr = curr.next
            i+=1
        print(i)
        return curr.val if (curr and i == index) else -1
            
        
        

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        temp = self.head
        self.head = ListNode(val)
        self.head.next = temp
        
    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        """
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(val)
        
        

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        curr = self.head
        i = 0
        if index == 0:
            self.addAtHead(val)
            return
        while curr.next and i < index-1:
            curr = curr.next
            i+=1
        if not curr.next and i == index-1:
            curr.next = ListNode(val)
        elif not curr.next and i < index-1:
            return
        else:
            temp = curr.next
            curr.next = ListNode(val)
            curr.next.next = temp
        
            
        
        

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        curr = self.head
        prev = None
        i = 0
        if index == 0:
            self.head = self.head.next
            return
        while curr.next and i < index:
            prev = curr
            curr = curr.next
            i+=1
        if i == index and curr != None:
            prev.next= curr.next
    
        

#Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.addAtIndex(0,10)
obj.addAtIndex(0,20)
obj.addAtIndex(1,10)
obj.deleteAtIndex(2)
obj.addAtHead(6)
obj.addAtTail(4)
print(obj.get(4))

#print(obj.get(1))