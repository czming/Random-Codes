import sys

sys.setrecursionlimit(100000)

class GraphNode:
    #for multiple loops
    def __init__(self, self_id):
        assert type(self_id) == int
        self.id = self_id
        #key will be the id and the value will be a pointer to the neighbour itself
        self.neighbours = {}
    def add_neighbours(self, new_neighbour, weight = 1):
        self.neighbours[new_neighbour] = weight
    def get_neighbours(self):
        return self.neighbours
    def get_id(self):
        return self.id
    def change_neighbour(self, old_neighbour, new_neighbour):
        #change all the pointers over
        if new_neighbour == self.id:
            #cannot add a self loop for the Karger algorithm
            #but stil need to get rid of the old neighbour, so it's like pointing to yourself then deleting the self loop
            del (self.neighbours[old_neighbour])
            return False
        if self.neighbours.get(old_neighbour):
            #need to change all the pointers from the old neighbour to new neighbour
            #only if can find old neighbour
            if self.neighbours.get(new_neighbour):
                self.neighbours[new_neighbour] += self.neighbours[old_neighbour]
            else:
                self.neighbours[new_neighbour] = self.neighbours[old_neighbour]
            del (self.neighbours[old_neighbour])
            return self.neighbours[new_neighbour]
        else:
            #cannot find old_neighbour
            return False
    def delete_neighbour(self, neighbour):
        if self.neighbours.get(neighbour):
            del (self.neighbours[neighbour])
            return True
        else:
            return False

class Graph:
    def __init__(self):
        self.graph = {}
        self.ordering = []
        self.explored = {}

    def insert_node(self, node):
        #it is a node, just input directly
        if type(node) == GraphNode:
            self.graph[node.get_id()] = node
        elif type(node) == int:
            #just an integer, insert empty node with integer as id
            new_node = GraphNode(node)
            self.graph[node] = new_node

    def add_edge(self, start_node, end_node, weight = 1):
        #crete the missing nodes
        if not self.graph.get(start_node):
            self.insert_node(start_node)
        if not self.graph.get(end_node):
            self.insert_node(end_node)
        self.graph[start_node].add_neighbours(end_node)

    def get_graph(self):
        return self.graph

    def size(self):
        return len(self.graph)

    def depth_first_search(self, start_vertex, order = False):
        #depth first search from a vertex for kasaraju (need to set ordering)
        if self.explored.get(start_vertex):
            return 0
        stack = [start_vertex]
        self.explored[start_vertex] = True
        size = 0
        while len(stack) >= 1:
            #just see the last element, don't pop yet
            curr = stack[-1]
            #see if it still had children to explore
            children = False
            for i in self.graph[curr].get_neighbours():
                #go through all its children first
                if not self.explored.get(i):
                    #indicate that curr_vertex has been explored so it will not be searched again
                    #placed here before actually searching it to prevent double count when searching its siblings
                    self.explored[i] = True
                    children = True
                    stack.append(i)
                    #add one when this depth first search comes across another unexplored element
                    size += 1
            #add itself after adding all its children, so must have no children left
            if order and not children:
                #want to track ordering, only store ordering for the call that needs it
                self.ordering.append(curr)
            if not children:
                #no children, pop that element
                stack.pop()

        #plus one for the start vertex
        return size + 1

    def get_ordering(self):
        return self.ordering

    def kasaraju(self):
        #reverse edges of graph
        new_graph = Graph()
        for i in self.graph:
            for j in self.graph[i].get_neighbours():
                #reverse the order
                new_graph.add_edge(j, i)
        print ("Test")
        for i in self.graph:
            #go through all nodes in the list that haven't been ordered
            new_graph.depth_first_search(i, order = True)
        print ("test")
        leaders = {}
        #reverse the ordering
        for i in new_graph.get_ordering()[::-1]:
            if not self.explored.get(i):
                #not searched yet
                leaders[i] = self.depth_first_search(i)
            
        return leaders
        
with open("SCC.txt", "r") as infile:
    infile = [[int(j) for j in i.split()] for i in infile.readlines()]

##infile = [[1,9], [9,5], [5,7], [7,1], [9,2], [2,3],[3,4],[4,2], [4,13], [2,12], [13,11], [12,11], [13,2], [13,12]]

g = Graph()
for i in infile:
    g.add_edge(i[0], i[1])
    
leaders = g.kasaraju()
