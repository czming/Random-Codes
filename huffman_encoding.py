from heap import MinHeap

class HCMiddleNode:
    #intermediate node for huffman encoding
    def __init__(self, child1, child2):
        #children should be either a leaf or a middle node
        self.children = [child1, child2]
        self.frequency = child1.get_frequency() + child2.get_frequency()

    def get_children(self):
        return self.children

    def get_frequency(self):
        return self.frequency

    def add_prefix(self, character):
        for i in self.children:
            i.add_prefix(character)

    def print_children(self):
        for i in self.children:
            i.print_children()

    def find_shortest(self):
        left = self.children[0].find_shortest()
        right = self.children[1].find_shortest()
        if left < right:
            return left
        return right

    def find_longest(self):
        left = self.children[0].find_longest()
        right = self.children[1].find_longest()
        if left > right:
            return left
        return right

    
class HCLeafNode:
    def __init__(self, character, frequency):
        self.character = character
        self.frequency = frequency
        self.encoding = ""
        
    def add_prefix(self, character):
        #polymorphism with HCMiddleNode class
        self.encoding = character + self.encoding

    def get_frequency(self):
        #polymorphism with HCMiddleNode class
        return self.frequency

    def __eq__(self, other):
        return self.character == other

    def print_children(self):
        print (self.character, self.frequency, self.encoding)

    def find_shortest(self):
        return len(self.encoding)

    def find_longest(self):
        return len(self.encoding)

with open("huffman.txt", "r") as infile:
    infile = [int(i) for i in infile.readlines()[1:]]
    infile = list(enumerate(infile))

##infile = [(0,1), (1,5), (2,7), (3,2), (4,3)]

min_heap = MinHeap()
for i in infile:
    min_heap.insert(i[1], HCLeafNode(i[0], i[1]))

#do until only one node left, the root
while min_heap.size() > 1:
    #get two smallest nodes
    small = min_heap.pop().get_data()
    small.add_prefix("0")
    two_small = min_heap.pop().get_data()
    two_small.add_prefix("1")
    #merge them together
    merged = HCMiddleNode(small, two_small)

    min_heap.insert(merged.get_frequency(), merged)

tree = min_heap.pop().get_data()
