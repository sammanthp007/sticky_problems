# Given an array of integers, return the highest product possible by multiplying 3 numbers from the array

# input - a list of integers, n
# output - a number that has the highest product

# working:
# find the highest 3 items and find the highest 2 negative numbers

def max_prod_n(lis, n):
    if n >= len(lis):
        return 0
    sorted_lis = lis[:n]
    sorted_lis.sort()
    neg_lis = lis[:2]
    neg_lis.sort()
    # find the highest 3
    for num_index in range(0, len(lis)):
        if lis[num_index] > sorted_lis[0]:
            sorted_lis.pop(0)
            sorted_lis.append(lis[num_index])
            sorted_lis.sort()
    # find the lowest negative number
    for num_index in range(2, len(lis)):
        if lis[num_index] < neg_lis[1]:
            neg_lis.pop()
            neg_lis.append(lis[num_index])
            neg_lis.sort()
    # calculate the product of the largest three number
    pos = 1
    for item in sorted_lis:
        pos *= item
    # calculate the product of the largest num and the smallest two negative number
    neg = 1
    for item in neg_lis:
        neg *= item
    neg *= sorted_lis[-1]
    # compare the two cases and return the larger result
    if pos > neg:
        return pos
    return neg

lis = [ 32, -92, -18, -94, -33, 27, 77, -15 ]
print (max_prod_n(lis, 3))
