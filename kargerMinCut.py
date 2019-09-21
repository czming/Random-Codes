from random import randint
from copy import deepcopy

class GraphNode:
    #for multiple loops
    def __init__(self, self_id):
        assert type(self_id) == int
        self.id = self_id
        #key will be the id and the value will be a pointer to the neighbour itself
        self.neighbours = {}
    def add_neighbours(self, new_neighbours):
        if type(new_neighbours) == list:
            #if list then go through the list
            for i in new_neighbours:
                if self.neighbours.get(i):
                    self.neighbours[i] += 1
                else:
                    self.neighbours[i] = 1

        elif type(new_neighbours) == dict:
            #for dict, add the number of connections over
            for i in new_neighbours.keys():
                if self.neighbours.get(i):
                    self.neighbours[i] += new_neighbours[i]
                else:
                    self.neighbours[i] = new_neighbours[i]
        else:
            #only one object, just add
            if self.neighbours.get(new_neighbours):
                #already a neighbour
                self.neighbours[new_neighbours] += 1
            else:
                self.neighbours[new_neighbours] = 1
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

    def insert_node(self, node):
        #it is a node, just input directly
        if type(node) == GraphNode:
            self.graph[node.get_id()] = node
        elif type(node) == int:
            #just an integer, insert empty node with integer as id
            new_node = GraphNode(node)
            self.graph[i] = new_node

    def fuse_nodes(self, node1, node2):
        #assumes input is int
        assert type(node1) == int and type(node2) == int
        #fuse everything into node1 then delete node2
        #get all the neighbours of node2 to use their edges with node2 to point at node1 instead
        #same thing for node1
        node1 = self.graph[node1]
        node2 = self.graph[node2]
        #delete each other's pointers so no self loops when merging or pointing to the non existent pointer 2 after that
        node1.delete_neighbour(node2.get_id())
        node2.delete_neighbour(node1.get_id())
        #add node2's neighbours to node1
        node1.add_neighbours(node2.get_neighbours())
        for i in node2.get_neighbours():
            curr_node = self.graph[i]
            #change from node2 to node1
            curr_node.change_neighbour(node2.get_id(), node1.get_id())
        del(self.graph[node2.get_id()])

    def get_graph(self):
        return self.graph

    def size(self):
        return len(self.graph)

    def get_crossing_edges(self):
        if self.size() != 2:
            #cannot get crossing edges from a graph that is not a cut, i.e. 2 nonempty sets
            return -1
        else:
            group_one = self.graph[list(self.graph)[0]]
            group_one_neighbours = group_one.get_neighbours()
            return group_one_neighbours[list(group_one_neighbours)[0]]
            
#THOUGHTS: Each edge does not have equal probability of being selected, instead it is the nodes that have equal probability
#of being selected in the first step (for the second step, it is nodes that have more edges that have high probability of being selected)
#so edges connected to nodes with less edges have higher probability of being selected (since equal probability of vertex being selected
#but less edges to select in the second step


g = Graph()

with open("kargerMinCut.txt", "r") as infile:
    infile = [[int(j) for j in i.split()] for i in infile.readlines()]
    for i in infile:
        new_node = GraphNode(i[0])
        new_node.add_neighbours(i[1:])
        g.insert_node(new_node)

###test code
##gn1 = GraphNode(1)
##gn2 = GraphNode(2)
##gn3 = GraphNode(3)
##gn1.add_neighbours([2,2])
##gn2.add_neighbours([1,1])
##g = Graph()
##g.insert_node(gn1)
##g.insert_node(gn2)
##g.insert_node(gn3)
##g.fuse_nodes(3,1)
###should only point to id 2
##print (g.get_graph()[3].get_neighbours())
##g.fuse_nodes(3, 2)
###should be nothing since no self loop
##print (g.get_graph()[3].get_neighbours())

min_cut = float("inf")
i = 0
while True:
    temp_g = deepcopy(g)
    while temp_g.size() > 2:
        #while more than 2 nodes
        curr_graph = temp_g.get_graph()
        random_one = list(curr_graph)[randint(0,len(curr_graph)-1)]
        random_one_neighbours = curr_graph[random_one].get_neighbours()
        random_two = list(random_one_neighbours)[randint(0,len(random_one_neighbours.keys())-1)]
        temp_g.fuse_nodes(random_one, random_two)
    i += 1
    if temp_g.get_crossing_edges() < min_cut:
        min_cut = temp_g.get_crossing_edges()
        print (min_cut, i)
        
