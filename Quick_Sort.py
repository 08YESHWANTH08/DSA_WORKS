def partition(array,lb,ub):
    #chose the rightmost element as pivot
    pivot = array[ub]
    #getting index of rightmost element
    i = lb - 1
    #traversing array from left to right
    for j in range(lb, ub):
        #getting the index of first element which is greater than pivot from left side as i
        if array[j] <= pivot:
            i = i + 1
            #swapping element in the index i and first element which is lesser than pivot from rightmost 
            array[i], array[j] = array[j], array[i]
    #swapping element in i+1 which is greater than ub when i<ub
    array[i + 1], array[ub] = array[ub], array[i + 1]
    #returning the index of pivot at which all the elements which left to pivot is less than pivot
    #and right to pivot is greater than pivot
    return i + 1
def quicksort(array,lb,ub):
    if(lb<ub):
        #stores partition of array as lock
        lock=partition(array,lb,ub)
        #sort the sub-array which is left to pivot recursively
        quicksort(array,lb,lock-1)
        #sort the sub-array which is right to pivot recursively
        quicksort(array,lock+1,ub)
array=list(map(int,input("Enter Array Elements (With Space): ").split(" ")))
quicksort(array,0,len(array)-1)
print(f"Sorted Array: {array}")
