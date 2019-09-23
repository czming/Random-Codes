from heap import MinHeap
from collections import defaultdict

#weighted graph
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
        self.graph[start_node].add_neighbours(end_node, weight)

    def get_graph(self):
        return self.graph

    def size(self):
        return len(self.graph)


g = Graph()

with open("dijkstraData.txt", "r") as infile:
    infile = [[j.split(",") for j in i.split()] for i in infile.readlines()]

for i in infile:
    curr = int(i[0][0])
    for j in i[1:]:
        g.add_edge(curr, int(j[0]), int(j[1]))


minheap = MinHeap()

start_vertex = 1
#store shortest distances, by default is infinite length to reach
shortest_distance = {start_vertex: 0}
added_vertices = [1]
curr = start_vertex
curr_vertex = g.get_graph()[curr]
for neighbour, weight in curr_vertex.get_neighbours().items():
    #key is the weight of getting to each vertex in the unexplored area
    #first vertex in data is the source and second is the destination
    minheap.insert(weight, curr, neighbour)


while not minheap.is_empty():
    popped = minheap.pop()
    curr = popped.get_data()[1]
    if curr in shortest_distance:
        #just delete and move on since this vertex has already been seen
        continue
    #the vertex from the searched that points to the new element
    curr_parent = popped.get_data()[0]
    #add current vertex to shortest distance so the distance has been set
    shortest_distance[curr] = popped.get_key()
    for neighbour, weight in g.graph[curr].get_neighbours().items():
        #popping from min heap and ignoring those that were seen before, so the shortest paths will keep coming up first, so no need to delete
        #the check if curr in shortest distance also ensures that our duplicate entries for same vertex will be ignored since they would
        #have previously been inserted into minheap

        #for below, new distance to each neighbour from the current would be the shortest distance to current + weight of edge between them
        minheap.insert(shortest_distance[curr] + weight, curr, neighbour)
