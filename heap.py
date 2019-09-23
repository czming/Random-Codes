#implementation of heap to be imported by other code
class MinHeap:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def peek(self):
        if self.is_empty():
            return -1
        return self.heap[0]

    def size(self):
        return len(self.heap)


    def insert(self, key, *data):
        new_node = HeapNode(key, data)
        self.heap.append(new_node)
        #current index
        curr = len(self.heap) - 1
        self.swap_up(curr)

    def pop(self):
        #delete the first node (i.e. smallest element)
        if self.is_empty():
            return -1

        elif len(self.heap) == 1:
            #last element
            popped_element = self.heap.pop()
            return popped_element
        popped_element = self.heap[0]

        #replace top element with bottom element in heap
        self.heap[0] = self.heap.pop()

        curr = 0
        self.swap_down(curr)
        
        return popped_element

    def delete(self, element, data = False, index = 0):
        #data argument specifies if we are looking for the element based on data
        #and index specifies the column
        if self.is_empty():
            return -1
        i = 0
        #search for the element in data array
        if data:
            #look through data, by default, first element as default value of index is 0
            while i < len(self.heap) and self.heap[i].get_data()[index] != element:
                i += 1            
        else:
            while i < len(self.heap) and self.heap[i] != element:
                i += 1

        #finds first element then escapes while loop to be deleted
                
        if i == len(self.heap):
            #reached end without finding the element
            return -1

        if i == len(self.heap) - 1:
            #last element, can just be deleted, will lead to error if not caught at self.heap[i] = self.heap.pop()
            #since self.heap[len(self.heap) - 1] will be deleted by then
            return self.heap.pop()
        

        #get element that was deleted
        deleted_element = self.heap[i]
        
        #delete last element and set the current element's position to the last element
        self.heap[i] = self.heap.pop()

        #check up and check down to ensure element is greater than new parent and smaller than children
        curr = i
        parent = (curr - 1) // 2
        left = curr * 2 + 1
        right = curr * 2 + 2
        self.swap_up(curr)
        self.swap_down(curr)

        return deleted_element
        
    def swap_down(self, curr):
        #checks and swaps curr element downwards until correct location is reached
        left = curr * 2 + 1
        right = curr * 2 + 2

        #when there isn't a left child, then there isn't a right child
        #and when there are no more children, no need to check any further
        while right < len(self.heap):
            if self.heap[left] < self.heap[right] and self.heap[left] < self.heap[curr]:
                #left is smaller than right and smaller than curr
                self.heap[left], self.heap[curr] = self.heap[curr], self.heap[left]
                curr = left

            elif self.heap[right] <= self.heap[left] and self.heap[right] < self.heap[curr]:
                #right is smaller than left, one of them needs to be equal to, otherwise
                #if left == right then both statements will be false
                self.heap[right], self.heap[curr] = self.heap[curr], self.heap[right]
                curr = right
            else:
                #both not smaller than curr, terminate
                break
                        #set new left and right child based on curr
            left = curr * 2 + 1
            right = curr * 2 + 2
            
        #need check if there's a left child
        if left < len(self.heap):
            if self.heap[left] < self.heap[curr]:
                #if only left child, it will not have any further children (since we add to the end of the array and delete from it as well)
                self.heap[left], self.heap[curr] = self.heap[curr], self.heap[left]

        #procedure, no return value
        return 0

    def swap_up(self, curr):
        #parent of current index, if odd then curr - 1 / 2, if even then curr/2
        #based on 1-indexing, start nodes of each layer is 1,2,4,8,etc.
        #for 0 indexing, just minused one from curr to get similar result
        parent = (curr - 1) // 2
        while self.heap[curr] < self.heap[parent] and curr > 0:
            #when curr = 0 means at root node, if allow that, it will wraparound the list
            #while before root and curr element is less than parent (for min heap ) and more than parent
            #for max heap
            self.heap[curr], self.heap[parent] = self.heap[parent], self.heap[curr]
            curr = parent
            parent = (curr - 1) // 2
        #after swapping up, the other child might be smaller than curr, e.g. 4 -> 3 <- 5, if 3 and 4 swap, 4 will be smaller than 5
        #and need to be swapped down
        self.swap_down(curr)

    def in_heap(self, element, data = False, index = 0):
        if data:
            #search through each element's data
            for i in self.heap:
                if i.get_data()[index] == element:
                    return i
            return -1
        for i in self.heap:
            if i.get_key() == element:
                return i
        return -1

    def print_heap(self):
        for i in self.heap:
            print(i.get(), end = " ")
        print ()

class MaxHeap:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def peek(self):
        if self.is_empty():
            return -1
        return self.heap[0]

    def size(self):
        return len(self.heap)


    def insert(self, key, *data):
        new_node = HeapNode(key, data)
        self.heap.append(new_node)
        #current index
        curr = len(self.heap) - 1
        self.swap_up(curr)

    def pop(self):
        #delete the first node (i.e. smallest element)
        if self.is_empty():
            return -1

        elif len(self.heap) == 1:
            #last element
            popped_element = self.heap.pop()
            return popped_element
        popped_element = self.heap[0]

        #replace top element with bottom element in heap
        self.heap[0] = self.heap.pop()

        curr = 0
        self.swap_down(curr)
        
        return popped_element

    def delete(self, element, data = False, index = 0):
        #data argument specifies if we are looking for the element based on data
        #and index specifies the column
        if self.is_empty():
            return -1
        i = 0
        #search for the element in data array
        if data:
            #look through data, by default, first element as default value of index is 0
            while i < len(self.heap) and self.heap[i].get_data()[index] != element:
                i += 1            
        else:
            while i < len(self.heap) and self.heap[i] != element:
                i += 1

        #finds first element then escapes while loop to be deleted
                
        if i == len(self.heap):
            #reached end without finding the element
            return -1

        if i == len(self.heap) - 1:
            #last element, can just be deleted, will lead to error if not caught at self.heap[i] = self.heap.pop()
            #since self.heap[len(self.heap) - 1] will be deleted by then
            return self.heap.pop()
        

        #get element that was deleted
        deleted_element = self.heap[i]
        
        #delete last element and set the current element's position to the last element
        self.heap[i] = self.heap.pop()

        #check up and check down to ensure element is greater than new parent and smaller than children
        curr = i
        parent = (curr - 1) // 2
        left = curr * 2 + 1
        right = curr * 2 + 2
        self.swap_up(curr)
        self.swap_down(curr)

        return deleted_element
        
    def swap_down(self, curr):
        #checks and swaps curr element downwards until correct location is reached
        left = curr * 2 + 1
        right = curr * 2 + 2

        #when there isn't a left child, then there isn't a right child
        #and when there are no more children, no need to check any further
        while right < len(self.heap):
            if self.heap[left] > self.heap[right] and self.heap[left] > self.heap[curr]:
                #left is smaller than right and smaller than curr
                self.heap[left], self.heap[curr] = self.heap[curr], self.heap[left]
                curr = left

            elif self.heap[right] >= self.heap[left] and self.heap[right] > self.heap[curr]:
                #right is smaller than left, one of them needs to be equal to, otherwise
                #if left == right then both statements will be false
                self.heap[right], self.heap[curr] = self.heap[curr], self.heap[right]
                curr = right
            else:
                #both not smaller than curr, terminate
                break
                        #set new left and right child based on curr
            left = curr * 2 + 1
            right = curr * 2 + 2
            
        #need check if there's a left child
        if left < len(self.heap):
            if self.heap[left] > self.heap[curr]:
                #if only left child, it will not have any further children (since we add to the end of the array and delete from it as well)
                self.heap[left], self.heap[curr] = self.heap[curr], self.heap[left]

        #procedure, no return value
        return 0

    def swap_up(self, curr):
        #parent of current index, if odd then curr - 1 / 2, if even then curr/2
        #based on 1-indexing, start nodes of each layer is 1,2,4,8,etc.
        #for 0 indexing, just minused one from curr to get similar result
        parent = (curr - 1) // 2
        while self.heap[curr] > self.heap[parent] and curr > 0:
            #when curr = 0 means at root node, if allow that, it will wraparound the list
            #while before root and curr element is less than parent (for min heap ) and more than parent
            #for max heap
            self.heap[curr], self.heap[parent] = self.heap[parent], self.heap[curr]
            curr = parent
            parent = (curr - 1) // 2
        #after swapping up, the other child might be smaller than curr, e.g. 4 -> 3 <- 5, if 3 and 4 swap, 4 will be smaller than 5
        #and need to be swapped down
        self.swap_down(curr)

    def in_heap(self, element, data = False, index = 0):
        if data:
            #search through each element's data
            for i in self.heap:
                if i.get_data()[index] == element:
                    return i
            return -1
        for i in self.heap:
            if i.get_key() == element:
                return i
        return -1

    def print_heap(self):
        for i in self.heap:
            print(i.get(), end = " ")
        print ()



#just a nice wrapper, can be replaced with a 1D array with a dictionary
class HeapNode:
    def __init__(self, key, data=[]):
        self.key = key
        self.data = data
    
    def get(self):
        return (self.key, self.data)

    def get_data(self):
        return self.data

    def get_key(self):
        return self.key

    def __eq__(self, other):
        #for x == y
        return self.key == other

    def __lt__(self, other):
        # For x < y
        return self.key < other
    
    def __le__(self, other):
        # For x <= y
        return self.key <= other
    
    def __ne__(self, other):
        # For x != y OR x <> y
        return self.key != other
    
    def __gt__(self, other):
        # For x > y
        return self.key > other
    
    def __ge__(self, other):
        #For x >= y
        return self.key >= other

#test code
from random import randint

a = MinHeap()
array = [a.insert(randint(1,1000), [i, i+1]) for i in range(1000)]
##prev = a.pop()
##for i in range(1000):
##    curr = a.pop()
##    #for max heap
##    if prev < curr:
##        print ("prev smaller than curr")
##    prev = curr
##print ("completed")
