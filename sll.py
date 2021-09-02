'''
Singly Linked sll
8/19/21
Edel Barcenas
'''

class Node:
    def __init__(self, val, next):
        self.val = val;
        self.next = next;

class SLL:
    def __init__(self):
        self.head = None;

    def add_helper(self, node, val):
        if node is None: return Node(val, None);
        else: node.next = self.add_helper(node.next, val); return node;
    def add(self, val):
        self.head = self.add_helper(self.head, val);

    def close_helper(self, node):
        if node is None: return self.head;
        else: node.next = self.close_helper(node.next); return node;
    def close(self): # creates a circular linked list
        self.head = self.close_helper();

    def contains(self, val):
        temp = self.head;
        while True:
            if temp is None: return False;
            elif temp.val == val: return True;

    def is_empty(self):
        if self.head is None: return True;
        return False;

    def remove_helper(self, node, val):
        if node is None: return None;
        elif node.val == val: return node.next;
        else:
            node.next = self.remove_helper(node.next, val);
            return node;
    def remove(self, val):
        self.head = self.remove_helper(self.head, val);


    def display(self):
        temp = self.head;
        while True:
            if temp is None: break;
            print(temp.val);
            temp = temp.next;

def test():
    sll = SLL();

    sll.add(1);
    sll.display(); print();
    sll.add(2);
    sll.add(3);
    sll.display(); print();
    sll.remove(2);
    sll.display();

#test();
