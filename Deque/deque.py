class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.pre = None

class Deque:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.length = 0


    def add_last(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        new_node = ListNode(x)
        if not self.head:
            self.head = new_node
        else:
            tmp = self.head
            while tmp.next:
                tmp = tmp.next
            new_node.pre = tmp
            tmp.next = new_node


        self.length += 1
        
    def add_first(self, x:int) -> None:
        """
        Push element x to the head of queue.
        """
        new_node = ListNode(x)
        if not self.head:
            self.head = new_node
        else:
            tmp = self.head
            self.head = new_node
            self.head.next = tmp
            tmp.pre = self.head
            
        self.length += 1

    def remove_first(self) -> None:
        """
        Removes the element from in front of queue
        """
        if not self.head:
          return

        old_head = self.head
        self.head = old_head.next if old_head.next else None

        if self.head:
            self.head.pre = None
        self.length -= 1
    
    def remove_last(self) -> None:
        """
        Removes the last element
        """
        if not self.head:
          return

        tmp = self.head
        while tmp.next:
          tmp = tmp.next
        
        pre_tmp = tmp.pre
        pre_tmp.next = None
        self.length -= 1

    def peek_first(self) -> int:
        """
        Get the front element.
        """
        return self.head.val if self.head else -1
    
    def peek_last(self) -> int:
        """
        Get the Last element.
        """
        if not self.head:
          return -1
        
        tmp = self.head
        while tmp.next:
          tmp = tmp.next

        return tmp.val

    def size(self) -> int:
        """
        Returns length of the queue
        """
        return self.length



# test
obj = Deque()
obj.add_first(1)
obj.add_last(2)
print(obj.peek_first())
print(obj.peek_last())
print(obj.size())

obj.remove_first()
print(obj.peek_first())
obj.add_first(1)
obj.remove_last()
print(obj.peek_first())

obj.remove_first()
obj.remove_first()
obj.remove_first()
print(obj.size())