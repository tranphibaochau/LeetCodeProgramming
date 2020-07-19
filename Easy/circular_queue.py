class MyCircularQueue:

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.size = 0
        self.array = [None]*k
        self.head_index = 0
        self.tail_index = 0
        

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if type(value) != int:
            print("Cannot add non-integers into queue")
            return False
        if self.size == 0:
            self.array[self.head_index] = value
        else:
            if self.size == len(self.array):
                print("It's full, popping the head before adding another element")
                self.deQueue()
            self.tail_index += 1
            self.tail_index = self.tail_index % len(self.array)
            self.array[self.tail_index] = value
        self.size+=1
        return True


    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.size == 0:
            return False
        else:
            self.array[self.head_index] = None
            self.head_index +=1
            self.head_index = self.head_index % len(self.array)
            self.size -=1
            return True


        

    def Front(self):
        """
        Get the front item from the queue.
        """
        if self.size == 0:
            return -1
        return self.array[self.head_index]
        

    def Rear(self):
        """
        Get the last item from the queue.
        """
        if self.size == 0:
            return -1
        return self.array[self.tail_index]

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        """
        return self.size == 0

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        """
        return self.size == len(self.array)
    def printQueue(self):
        if self.head_index > self.tail_index:
            for i in range(self.head_index, (self.tail_index +len(self.array))+1):
                index = i % len(self.array)
                print (self.array[index], end=" ")
        else:
            for i in range(self.head_index, (self.tail_index)+1):
                print (self.array[i], end=" ")
        print()
        print("Front: ", self.Front())
        print("Rear: ", self.Rear())




# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(5)
obj.enQueue(9)
obj.enQueue(10)
obj.enQueue(20)
obj.enQueue(14)
obj.enQueue(50)
obj.printQueue()
obj.deQueue()
obj.deQueue()
obj.printQueue()
obj.enQueue(90)
obj.enQueue(30)
obj.printQueue()
param_2 = obj.deQueue()
obj.printQueue()
param_2 = obj.deQueue()
param_2 = obj.deQueue()
param_2 = obj.deQueue()
param_2 = obj.deQueue()
obj.printQueue()
print("IsEmpty: ", obj.isEmpty())