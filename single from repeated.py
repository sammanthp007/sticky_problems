# Given an array of integers, every element appears twice except for one. Find that single one.
# @param A : array of integers
    # @return an integer
def singleNumber(A):
    A = sorted(A)
    for index in range(0, len(A), 2):
        if not (A[index] == A[index + 1]):
            return A[index]

# using xor:

lis = [2,2,4,1,5,4,1]
def single_number_xor(lis):
    res = 0
    for item in lis:
        res ^= item
    return res

# print (single_number_xor(lis))

