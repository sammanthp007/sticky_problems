# with a space complexity of O(1)
# implement a quick sort

def quick_sort(lis, start, end):
    # as long as there is a list
    if start < end:
        # puts the pivot in its position and gives the index where the pivot is
        partition_index = partition(lis, start, end)
        # get the item in the left array from pivot to get its pivot to its correct position
        quick_sort(lis, start, partition_index - 1)
        # make the pivot of the array to the right reach its correct position
        quick_sort(lis, partition_index + 1, end)
    
def partition(lis, start, end):
    # take the last element to be the pivot
    pivot = lis[end]
    # this is the index of the boundry, where the pivot will be substituted in the end
    partition_index = start
    for i in range(start, end):
        # if the current item is less than the pivot value, then swap the item in boundry pointer with it and increase the boundry pointer by one as it now contains an item that is less than our pointer
        if lis[i] <= pivot:
            swap(lis, partition_index, i)
            partition_index += 1
    # finally swap the boundry element with our pivot value
    swap(lis, end, partition_index)
    # return the position of the pivot as it should be in
    return partition_index

def swap(lis, a, b):
    lis[a], lis[b] = lis[b], lis[a]
    
lis = [2,1,5,3,4,7,6]
quick_sort(lis, 0, len(lis) - 1)
print (lis)