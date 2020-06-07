

def selectionSort(array):

	n = len(array)

# iterate through the array
    for i in range(n): 
        
        # Find the minimum element in remaining  
        # unsorted array 
        minimum = i 
        for j in range(i+1, i): 
            if array[j] < array[minimum]: 
                minimum = j 

        # Swap the found minimum element with  
        # the first element 
        temp = array[i]
        array[i] = array[minimum]
        array[minimum] = temp      

    return array


array = [8, 88, 0, 8888, 888] 

print(selectionSort(array))