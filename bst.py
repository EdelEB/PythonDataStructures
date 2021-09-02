'''
Edel Barcenas
7/28/21
CS 356
HW_4_1 Binary Search Tree

goal: create a functioning binary search tree
purpose: understand how to manipulate/add/delete/find nodes in a binary search tree
'''
class Node:
    def __init__(self, key, value, left, right):
        self.key = key;         #english word
        self.value = value;     #latin word/words
        self.left = None;       #left child, before parent in alphabetical order
        self.right = None;      #right child, after parent in alphabetical order

class BST:
    def __init__(self):
        self.root = None

    def clear(self):
        self.root = None;

    def is_empty(self):
        if self.root is None: return True;
        return False;

    def contains_helper(self, node, key):
        if node is None:        return False;
        elif node.key == key:   return True;
        elif key < node.key:    return self.contains_helper(node.left, key);
        else:                   return self.contains_helper(node.right, key);
    def contains(self, key):
        return self.contains_helper(self.root, key);

    def put_helper(self, node, key, value):
        if node is None:        node = Node(key, value, None, None);
        elif key == node.key:   node.value = value;
        elif key < node.key:    node.left = self.put_helper(node.left, key, value);
        else:                   node.right = self.put_helper(node.right, key, value);
        return node;
    def put(self, key, value):
        self.root = self.put_helper(self.root, key, value);

    def get_helper(self, node, key):
        if node.key == key:
            return node.value;
        elif key < node.key:
            return self.get_helper(node.left, key);
        else:
            return self.get_helper(node.right, key);
    def get(self, key):
        if not self.contains(key): return None; # key is not in tree
        return self.get_helper(self.root, key);

    def find_min(self, node):
        while node.left is not None:
            node = node.left;
        return node;

    def find_max(self, node):
        while node.right is not None:
            node = node.right;
        return node;

    def remove_helper(self, node, key):
        if key == node.key:
            if node.left is None and node.right is None:
                node = None;
            elif node.left is None:
                node = node.right;
            elif node.right is None:
                node = node.left;
            else:
                curr_right = node.right;            # saves right subtree
                node = self.find_max(node.left);    # replaces target with max node in left sub tree
                node.right = curr_right;            # ensures right subtree is not lost
                node.left = self.remove_helper(node.left, node.key); # removes max from left sub tree
        elif key < node.key:
            node.left = self.remove_helper(node.left, key);
        else:
            node.right = self.remove_helper(node.right, key);
        return node;

    def remove(self, key):
        if not self.contains(key): return; # key does not exist in tree
        self.root = self.remove_helper(self.root, key);

    def keys_helper(self, node, arr):
        if node is None:
            return;
        self.keys_helper(node.left, arr);
        arr.append(node.key);
        self.keys_helper(node.right, arr);
        return arr;
    def keys(self):
        if self.is_empty(): return [];
        return self.keys_helper(self.root, []);

def test():

    tree = BST()
    tree.put("a", "abee");
    tree.put("a", "asee");
    tree.put("a", "aye")
    tree.put("d", "dee");
    tree.put("c", "see");
    tree.put("b", "bee");
    tree.put("e", "ee");
    tree.put("f", "ef");
    tree.put("g", "jee");
    tree.put("h", "ache");
    tree.put("i", "ay");

    for key in tree.keys():
        print(key, ": ", tree.get(key));
    print();

    print("e in tree: ", tree.contains('e'));
    print("e value: ", tree.get('e'),'\nRemove e');
    tree.remove('e');
    print('e in tree: ', tree.contains('e'));
    print("e value: ", tree.get('e'));
    print();

    for key in tree.keys():
        print(key, ": ", tree.get(key));

    print("ROOT: ",tree.root.key, "\nremove root");

    tree.remove('a');

    for key in tree.keys():
        print(key, ": ", tree.get(key));
    print("ROOT: ", tree.root.key);
    print("left: ", tree.root.left.key,  ", right: ", tree.root.right.key)

    print("max: ", tree.find_max(tree.root).key);
    tree.remove('i');

    for key in tree.keys():
        print(key, ": ", tree.get(key));
    print("ROOT: ", tree.root.key);
    print("left: ", tree.root.left.key,  ", right: ", tree.root.right.key)

#test();

