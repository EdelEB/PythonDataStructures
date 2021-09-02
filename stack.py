'''
stack using linked node implementation instead of array implementation

Edel Barcenas
8/20/21
'''

class Node():
    def __init__(self, val, next):
        self.val = val;
        self.next = next;

class Stack():
    def __init__(self):
        self.top = None;

    def pop(self):
        if self.top is None: return None;
        temp = self.top.val
        self.top = self.top.next;
        return temp;

    def push(self, val):
        if self.top is None: self.top = Node(val, None); return;
        self.top = Node(val, self.top);

def test():
    s = Stack();
    for i in range(5):
        s.push(i);
    for i in range(6):
        print(s.pop());

test();