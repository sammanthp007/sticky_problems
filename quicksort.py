# with a space complexity of O(1)
# implement a quick sort

def quick_sort(lis, start, end):
    if start < end:
        partition_index = partition(lis, start, end)
        quick_sort(lis, start, partition_index - 1)
        quick_sort(lis, partition_index + 1, end)
    
def partition(lis, start, end):
    pivot = lis[end]
    partition_index = start
    for i in range(start, end):
        if lis[i] <= pivot:
            swap(lis, partition_index, i)
            partition_index += 1
    swap(lis, end, partition_index)
    return partition_index

def swap(lis, a, b):
    lis[a], lis[b] = lis[b], lis[a]
    
lis = [2,1,5,3,4,7,6]
quick_sort(lis, 0, len(lis) - 1)
print (lis)