from heapq import *
import heapq

with open("median.txt", "r") as infile:
    infile = infile.readlines()
    infile = [int(i) for i in infile]

#infile = [1,6,4,5,2]
    
lower_heap = []
greater_heap = []
#median only takes on 1 value, if even, then take the lower number
curr_median = -1

median_sum = 0

for i in infile:
    #first element
    if curr_median == -1:
        curr_median = i
    else:
        #add to appropriate heap
        if i >= curr_median:
            heappush(greater_heap, i)
        else:
            lower_heap = lower_heap + [i]
            heapq._heapify_max(lower_heap)
        #need to push one element to the lower heap
        if len(greater_heap) > len(lower_heap) + 1:
            lower_heap = lower_heap + [curr_median]
            heapq._heapify_max(lower_heap)
            curr_median = heappop(greater_heap)

        #since we take the lower of the 2 medians if present, lower_heap should never
        #be larger than the greater_heap
        elif len(lower_heap) > len(greater_heap):
            heappush(greater_heap, curr_median)
            curr_median = heapq._heappop_max(lower_heap)            

    median_sum += curr_median
##    if len(lower_heap) > 0 and len(greater_heap) > 0:
##        print (f"{lower_heap[0]} {curr_median} {greater_heap[0]}")
print (f"Sum of medians: {median_sum}")
