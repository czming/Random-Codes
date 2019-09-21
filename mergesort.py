def mergesort(array):
    if len(array) <= 1:
        return array
    else:
        left = mergesort(array[:len(array)//2])
        right = mergesort(array[len(array)//2:])
        combined = []
        #counters
        i = 0
        j = 0
        #while the counter hasn't reached the end of the array
        while i < len(left) and j < len(right):
            #find lowest element and append (compare the elements)
            if left[i] < right[j]:
                combined.append(left[i])
                i += 1
            else:
                combined.append(right[j])
                j += 1
        if i == len(left):
            #reached end of left
            combined = combined + right[j:]
        else:
            #reached end of right
            combined = combined + left[i:]
        return combined
    
def inversions(array):
    if len(array) <= 1:
        return array, 0
    else:
        left, left_count = inversions(array[:len(array)//2])
        right, right_count = inversions(array[len(array)//2:])
        combined = []
        split_count = 0
        #counters
        i = 0
        j = 0
        #while the counter hasn't reached the end of the array
        while i < len(left) and j < len(right):
            #find lowest element and append (compare the elements)
            if left[i] < right[j]:
                combined.append(left[i])
                i += 1
            else:
                #right side, any of these get called, means inversion split across left and right
                #number of inversions is the number of elements remaining on left side, because these are the ones whose lines are intersected
                combined.append(right[j])
                j += 1
                #because index starts from 0 while len starts from 1, hence -1
                #above statement is wrong, because pointer i is pointing before the element, so if at len(left) - 1 means still have one element that hasn't been inserted yet
                split_count += (len(left) - i)
        if i == len(left):
            #reached end of left, right insertions are only noteworthy when they are crossing something in the left array
            combined = combined + right[j:]
        else:
            #reached end of right
            combined = combined + left[i:]
        return combined, left_count + right_count + split_count
