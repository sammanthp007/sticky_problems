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
def BinarySearchIterative(lis, key):
    last = len(lis) - 1
    first = 0
    while first <= last:
        mid = (first + last) // 2
        if len(lis) == 0:
            return False
        if len(lis) == 1:
            if lis[0] == key:
                return True
            return False
        if lis[mid] == key:
            return True
        elif lis[mid] < key:
            first = mid + 1
        else:
            last = mid - 1
    return False

lis = [2,5,7,8,9,23,54,76,79,89]
# print (BinarySearchIterative(lis,54))