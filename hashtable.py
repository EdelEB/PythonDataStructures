def is_prime(num):
    for i in range(2, num // 2 + 1):
        if num % i == 0: return False;
    return True;

def double_prime(num):
    num *= 2;
    while True:
        num += 1;
        if is_prime(num): return num;

class Element:
    def __init__(self, key, value):
        self.key = key;
        self.value = value;

class Hashtable:
    def __init__(self):
        self.length = 20011;
        self.arr = [None]*self.length;
        self.ecount = 0; # element count

    def hash(self, key):
        ret = 0;
        string = str(key)
        for i in range(len(string)):
            temp = ord(string[i]);
            ret += temp*i + temp;

        if ret > self.length-1: return ret % (self.length-1);
        return ret;

    def clear(self):
        self.arr = [None]*self.length;

    def contains_helper(self, index, step, key):  # step is the number being added to the current index ( this uses quadratic probing )
        if step == 0: step = 1;
        else: index += step; step += step;
        if index > self.length - 1: index %= self.length;  # make sure index is in bounds

        if self.arr[index] is None: return False;
        elif self.arr[index] == '_' or self.arr[index].key != key: return self.contains_helper(index, step, key);
        else: return True;

    def contains(self, key):
        index = self.hash(key);
        return self.contains_helper(index, 0, key);

    # finds index of key, returns None if key does not exist
    def find_index_helper(self, index, step, key): # step is the number being added to the current index ( this uses quadratic probing )
        if step == 0: step = 1;
        else: index += step; step += step;
        if index > self.length-1: index %= self.length; # make sure index is in bounds

        if self.arr[index] == '_' or self.arr[index].key != key: return self.find_index_helper(index, step, key);
        else: return index;

    def find_index(self, index, key):
        return self.find_index_helper(index, 0, key);

    # finds next empty slot
    def find_empty_helper(self, index, step):
        if step == 0: step = 1;
        else: index += step; step += step;

        if index > self.length-1: index %= self.length; # make sure index is in bounds

        if self.arr[index] is None or self.arr[index] == '_': return index;
        else: return self.find_empty_helper(index, step);

    def find_empty(self, index):
        return self.find_empty_helper(index, 0);

    def get(self, key):
        if not self.contains(key): return None;
        index = self.hash(key);
        return self.arr[self.find_index(index, key)].value;

    def grow(self):
        self.length = double_prime(self.length);
        temp = [];
        for e in self.arr:
            if e is not None and e != '_': temp.append(e);
        self.clear();
        for e in temp: self.put(e.key, e.value);

    def is_empty(self):
        for x in self.arr:
            if x is not None: return False;
        return True;

    def keys(self):
        ret_arr = [];
        for element in self.arr:
            if element is not None and element != '_':
                ret_arr.append(element.key);
        return ret_arr;

    def put(self, key, value):
        index = self.hash(key);
        if self.contains(key):
            index = self.find_index(index , key);
            self.arr[index].value = value;
        else:
            index = self.find_empty(index);
            self.arr[index] = Element(key, value);
            self.ecount+=1;
            if self.ecount > self.length//2 : self.grow();

    def remove(self, key):
        if not self.contains(key): return;
        index = self.hash(key);
        self.arr[self.find_index(index, key)] = '_'; # using '_' instead of None insures that it is always possible to reach keys when others are deleted
        self.ecount -= 1;
        if self.ecount < self.length // 6: self.shrink();

    def shrink(self):
        self.length = double_prime(self.length//4);
        temp = [];
        for e in self.arr:
            if e is not None and e != '_': temp.append(e);
        self.clear();
        for e in temp: self.put(e.key, e.value);
        
def test():
    table = Hashtable();
    print("length : ", table.length);

    print("keys : " , table.keys());

    table.put('motive', 1);
    table.put('unique', 2);

    print("keys : ", table.keys());

    print("contains motive: ", table.contains('motive'));

    print("get motive: ", table.get('motive'));
    print("get unique: ", table.get('unique'));

    table.remove('motive');
    print("motive removed\ncontains motive: ", table.contains("motive"));

    print("keys : " , table.keys());

    print("get unique: ", table.get('unique'));
    table.remove('unique');
    print("unique removed\ncontains unique: ", table.contains("unique"))

    print("keys : " , table.keys());

#test();

#print(double_prime(5000));