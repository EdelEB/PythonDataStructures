
'''
Edel Barcenas
7/13/21
CS435 HW_2

goal: create a double-ended-que (deque) / two way linked list
purpose: familiarize ourselves with data structure construction and nodes
'''

class Node:
    def __init__(self, val, next, prev):
        self.val = val;
        self.next = next;
        self.prev = prev;

class Deque:
    def __init__(self):
        self.head = None;
        self.tail = None;

    def push_front(self, val):
        node = Node(val, self.head, None );

        if self.is_empty():
            self.tail = node;
        else:
            self.head.prev = node;
        self.head = node;

    def push_back(self, val):
        node = Node(val, None, self.tail);

        if self.is_empty():
            self.head = node;
        else:
            self.tail.next = node;
        self.tail = node;

    def pop_front(self):
        if self.is_empty(): return "Error: Attempted to pop from empty Deque";

        ret = self.head.val;
        self.head = self.head.next;

        if not self.is_empty(): self.head.prev = None;
        return ret;

    def pop_back(self):
        if self.is_empty(): return "Error: Attempted to pop from empty Deque";

        ret = self.tail.val;
        self.tail = self.tail.prev;

        if not self.is_empty(): self.tail.next = None;
        return ret;

    def clear(self):
        self.head = self.tail = None;

    def is_empty(self):
        return self.head is None or self.tail is None;

'''
            tail < node > none
      none < head/tail > none 
      
'''

def main():
    d = Deque();
    '''
    for i in range(5):
        d.push_back(i);
        
    for i in range(6):
        print(str(d.pop_back())+ " ", end="");
    print();
    
    print(str(d.pop_back())+ " ", end="");
    print(str(d.pop_front())+ " ", end="");
    print();
    
    d.push_front(0)
    d.push_front(0)
    d.push_back(2)
    d.push_front(1)
    '''
    d.push_front(0)
    d.pop_front()
    d.push_back(1)

    node = d.head

    while node is not None:
        print("head:", node.val)
        node = node.next

    node = d.tail
    while node is not None:
        print("tail:", node.val)
        node = node.prev

main();