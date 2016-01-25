# binarysearch using recursion
def BinarySearch(lis, key):
    # case1 : lis is empty; then we return false
    if len(lis) == 0:
        return False
    # case 2 : lis has one item; then if key == lis[0]: return True else: return False
    if len(lis) == 1:
        if lis[0] == key:
            return True
        else:
            return False
    # case 0 : if type(key) != int: return False
    if type(key) != int:
        return False   
    # case 3: implement a binary search
    low = 0
    high = len(lis) - 1
    middle = high + low // 2
    if lis[middle] == key:
        return True
    elif key > lis[middle]:
        return BinarySearch(lis[middle + 1:], key)
    else:
        return BinarySearch(lis[:middle], key)
    # return a boolean value
    
# binary search iteratively
def binary_search(lis, num):
    top = len(lis)
    bottom = 0
    while bottom < top:
        middle = (top + bottom) // 2
        if lis[middle] == num:
            return middle
        elif lis[middle] < num:
            bottom = middle
        elif lis[middle] > num:
            top = middle
    return -1

lis = [2,4,6,7,9,23,35,56,67,78]
print (binary_search([], 67))

lis = [2,5,7,8,9,23,54,76,79,89]
# print (BinarySearchIterative(lis,54))


def binary_search(lis,n,l,h):
    if len(lis) == 0:
        return -1
    elif len(lis) == 1:
        if lis[0] == n:
            return 0
        return -1
    middle = (l + h) // 2
    if n == lis[middle]:
        return middle
    elif n > lis[middle]:
        return binary_search(lis, n, middle + 1, h)
    else:
        return binary_search(lis, n, l, middle - 1)

lis = [2,3,4,5,6,7,8,23,45,65,67,87]
print (binary_search(lis, 67, 0, len(lis) - 1))