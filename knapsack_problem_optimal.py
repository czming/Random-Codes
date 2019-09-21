from collections import defaultdict
import sys

sys.setrecursionlimit(20000000)

def knapsack_problem_optimal(sizes, values, capacity):
    global optimal
    #use a dict so no need to create all the instances for those capacities that are not used
    #0 capacity means can carry 0 elements so 0 value
    optimal = [{0:0} for j in sizes]
    #add in to teh zero index the array for when 0 elements in set
    optimal = [dict(zip([i for i in range(capacity + 1)], [0 for i in range(capacity + 1)]))] + optimal
    #for optimal implementation, we only look at those that are relevant
    #need a recursive call to go all the way down to see which are relevant
    #this function just initializes the optimal array
    knapsack_recursive(sizes, values, capacity)
    
    return optimal

def knapsack_recursive(sizes, values, capacity):
    #the number of elements that we are looking at
    curr_index = len(sizes)
    if optimal[curr_index - 1].get(capacity) == None:
        #need to make a recursive call to get answer
        knapsack_recursive(sizes[:-1], values[:-1], capacity)
    no_last = optimal[curr_index - 1][capacity]
    if sizes[curr_index - 1] > capacity:
        #size of last element larger than current capacity, definitely no last
        #element included, won't have negative looparound with dict implementation
        #but can have negative index which is not wanted either (negative index can exist in dict)
        optimal[curr_index][capacity] = no_last
        return 0
    
    if optimal[curr_index - 1].get(capacity - sizes[curr_index - 1]) == None:
        knapsack_recursive(sizes[:-1], values[:-1], capacity - sizes[curr_index - 1])
    incl_last = optimal[curr_index - 1][capacity - sizes[curr_index - 1]] + values[curr_index - 1]

    optimal[curr_index][capacity] = max(no_last, incl_last)
    return 0

##print (knapsack_problem_optimal(sizes = [1,2,5], values = [5,2,1], capacity = 3))

def reconstruct(sizes, values, capacity):
    #uses the optimal array so need to run knapsack_problem_recursive first to build that array
    independent_set = []
    for i in range(len(optimal)-1,-1,-1):
        if capacity - sizes[i-1] >= 0 and optimal[i][capacity] == optimal[i-1][capacity - sizes[i-1]] + values[i-1]:
            #the second case was selected, current element is inside, append to independent set
            #need make sure index is at least 0 so it doesn't return negative indices (which was averted earlier as well)
            independent_set.append(i)
            capacity -= sizes[i - 1]
    #everything except last element
    return independent_set
            

with open("knapsack1.txt", "r") as infile:
    infile = [i.split() for i in infile.readlines()]
    capacity = int(infile[0][0])
    values = [int(i[0]) for i in infile[1:]]
    weights = [int(i[1]) for i in infile[1:]]


print (knapsack_problem_optimal(weights, values, capacity)[len(weights)][capacity])
