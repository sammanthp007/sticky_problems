# write a function that takes an array A of length n and an index i into A, and rearranges the elements such that all elements less than A[i] appears first, followed by elements equal to A[i], followed by elements greater than A[i]. Your algorithm should have O(1) space complexity and O(n) time complexity.

# working:
# take the item at the index and put it in the end
partition_ptr = 0

def order(lis, index):
    partition_ptr = 0                           # keep track of where the larger valued items starts
    length = len(lis)
    swap(lis, index, length - 1)
    pivot = lis[-1]
    for element_index in range(length):
        if lis[element_index] < pivot:
            swap(lis, element_index, partition_ptr)
            partition_ptr += 1
    swap(lis, partition_ptr, length - 1)
    start = partition_ptr
    for element_index in range(partition_ptr + 1, length):
        if len(lis) > partition_ptr + 1 and lis[element_index] == lis[partition_ptr]:
            swap(lis, element_index, partition_ptr + 1)
            partition_ptr += 1

def swap(lis, a, b):
    lis[a], lis[b] = lis[b], lis[a]

lis = [3,4,2,6,2,7,4,8,2,25,4,6,8,9]
order(lis, 6)
print (lis)