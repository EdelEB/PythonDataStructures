'''
Edel Barcenas
8/1/21
CS 356
HW_5_1 Heap

goal: create a functioning heap data structure for general use
purpose: understand how to manipulate/add/delete nodes in a heap
'''

class Element:
    def __init__(self, element, priority):
        self.element = element;
        self.priority = priority;

class Heap: # min heap
    def __init__(self): self.data = [];

    def clear(self): self.data = [];

    def is_empty(self):
        if len(self.data) == 0: return True;
        return False;

    def parent(self, i): return (i-1)//2; # returns INDEX of parent

    def lchild(self, i): return i*2+1; # returns INDEX of left child

    def rchild(self, i): return i*2+2; # return INDEX of right child

    def float(self):
        i = len(self.data)-1;
        while i != 0:
            p = self.parent(i);
            if self.data[i].priority < self.data[p].priority:
                self.data[i], self.data[p] = self.data[p], self.data[i]; # swap with parent
                i = p;
            else:
                return;
        return;

    def sink_helper(self, i):
        length = len(self.data)-1;
        l = self.lchild(i);
        r = self.rchild(i);
        if l > length and r > length:   # l and r indexes out of bounds
            return;
        elif l > length:    # ONLY l index out of bounds
            if self.data[r].priority < self.data[i].priority:
                self.data[i], self.data[r] = self.data[r], self.data[i];  # swap with rchild
                return self.sink_helper(r);
        elif r > length:    # ONLY r index out of bounds
            if self.data[l].priority < self.data[i].priority:
                self.data[i], self.data[l] = self.data[l], self.data[i];  # swap with lchild
                return self.sink_helper(l);
        else:   # l and r are in bounds
            if self.data[l].priority < self.data[r].priority:   # priority l < r
                if self.data[l].priority < self.data[i].priority: # priority l < i
                    self.data[i], self.data[l] = self.data[l], self.data[i];  # swap with lchild
                    return self.sink_helper(l);
                return;
            elif self.data[r].priority < self.data[i].priority: # priority r < i
                self.data[i], self.data[r] = self.data[r], self.data[i];  # swap with rchild
                return self.sink_helper(r);
        return;

    def sink(self): # this can be done very similarly using iteration
        self.sink_helper(0);

    def enqueue(self, element, priority): # insert element (type Element)
        self.data.append(Element(element, priority));
        self.float();

    def dequeue(self):
        if self.is_empty(): return None;
        ret = self.data[0].element;                      # saves head element
        self.data[0] = self.data[len(self.data)-1]; # places last element into head
        self.data.pop(len(self.data)-1);            # deletes last element
        self.sink();
        return ret;

    def front(self):
        if self.is_empty(): return None;
        return self.data[0].element;

    def priority(self):
        if self.is_empty(): return None;
        return self.data[0].priority;

def test():

    heap = Heap();

    print("Empty? ", heap.is_empty());
    heap.enqueue('|||||||||', 9);
    heap.enqueue('|||||', 5);
    heap.enqueue('||||||||||', 10);
    heap.enqueue('||||||||', 8);
    heap.enqueue('|||||||', 7);

    #print("Empty? ", heap.is_empty(), '\nClear' );
    #heap.clear();
    print("Empty? ", heap.is_empty());

    print("top priority() & front() for [9,5,10,8,7]\n",heap.priority(), ' ', heap.front());

    heap.enqueue('|', 1);
    heap.enqueue('|||', 3);
    heap.enqueue('||||', 4);
    heap.enqueue('||||||', 6);
    heap.enqueue('||', 2);

    print("top priority() & front() for [9,5,10,8,7,1,3,4,6,2]\n", heap.priority(), ' ', heap.front());

    while not heap.is_empty():
        #for e in heap.data:
        #    print(e.priority, end="\t");
        print(heap.dequeue());
    print(heap.dequeue());  # dequeue empty heap

#test();