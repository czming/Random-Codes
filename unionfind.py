class UnionFind:
    def __init__(self, elements):
        #elements should be a 1 or 2D array
        for i in range(len(elements)):
            if type(elements[i]) != list:
                #wrap it with a list
                elements[i] = [elements[i]]
        self.groups = elements

    def find(self, element):
        #returns first group if multiple groups have same element
        return [i for i in range(len(self.groups)) if element in self.groups[i]][0]

    def union(self, group1, group2, is_element = False):
        #is_element specifies whether we want to merge groups with those elements instead
        if is_element:
            #find the elements' group
            group1 = self.find(group1)
            group2 = self.find(group2)
        self.groups[group1] = self.groups[group1] + self.groups[group2]
        del (self.groups[group2])

    def size(self):
        #return number of groups
        return len(self.groups)
