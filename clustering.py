from heap import MinHeap
from unionfind import UnionFind

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
        self.graph[start_node].add_neighbours(end_node, weight)

    def get_graph(self):
        return self.graph

    def size(self):
        return len(self.graph)

    def clustering(self, groups, minheap):
        #maxheap is a max heap of edges (one direction only)
        unionfind = UnionFind(list(self.graph.keys()))
        while unionfind.size() > groups:
            #keep merging until number of desired groups reached
            curr = minheap.pop()
            curr_edge = curr.get_data()
            if unionfind.find(curr_edge[0]) == unionfind.find(curr_edge[1]):
                #same group
                continue
            unionfind.union(curr_edge[0], curr_edge[1], True)
        while unionfind.find(curr_edge[0]) == unionfind.find(curr_edge[1]):
            #pop until different groups to get max distance, because next edge might be within a group
            minheap.pop().get_data()
            curr_edge = minheap.peek().get_data()

        #smallest distance is the edge at the top of max heap since they are in different groups
        return unionfind, minheap.peek().get_key()

g = Graph()
minheap = MinHeap()
    
with open("clustering1.txt", "r") as infile:
    infile = [[int(j) for j in i.split()] for i in infile.readlines()[1:]]

for i in infile:
    g.add_edge(i[0], i[1], i[2])
    #undirected graph, so add edge in the opposite direction
    g.add_edge(i[1], i[0], i[2])
    minheap.insert(i[2], i[1], i[0])

a = g.clustering(4, minheap)
