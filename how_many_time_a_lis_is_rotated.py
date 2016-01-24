# Given a sorted array of n integers that has been rotated an unknown number of
# times, give an O(log n) algorithm that finds an element in the array. You may assume
# that the array was originally sorted in increasing order.
# EXAMPLE:
# Input: find 5 in array (15 16 19 20 25 1 3 4 5 7 10 14)
# Output: 8 (the index of 5 in the array)

# input -> list, half sorted! -> binary search, 
# output -> an integer, index of the smallest element

# another interpretation: find the index of the minimum element
# test case: [15, 16, 19, 20, 25, 1,3 ,4 ,5 ,7 ,10 ,14]
        
#         -> the last index
#         [] -> ‘invalid’
#         -> the 0th index
#         -> 1
# -> half times = 4

# woking -> iterate from start to end comparing the index and index + 1, while index + 1 lasts
#         and if there is a decrease instead of an increase then we return the index + 1 value
# O(n), O(1)
# ________________________________
# working with binary:
# [2,3,4,5,7,0,1, 2, 2]

# middle  4   
# top 5
# bottom  4
# test = 7


def find_index_of_rotation(lis):
    top = len(lis) - 1
    bottom = 0
    if len(lis) < 2:
        return len(lis) - 1
    if len(lis) == 2:
        if lis[0] <= lis[1]:
            return 0
        else: 
            return 1
    test_val = lis[0]
    while bottom <= top:
        middle = (top + bottom) // 2
        if bottom + 1 == top:
            if lis[top] < lis[bottom]:
                return top
            elif lis[top] > lis[bottom]:
                return 0
        if test_val <= lis[middle]:# iit means that numbers are still increasing
            test_val = lis[middle]
            bottom = middle
        elif test_val > lis[middle]: # the rotation happened
            top = middle

# Test Cases:
# lis = [2,3,5,7,-2,0,1] # 4
# lis = [-3,-2,-1,-5,-4] # 3
# lis = [-3, -1, 23,45, -4] # 4
# lis = [1,2,3,4,5,6,7,8] # 0
# lis = [] # -1
# lis = [8,1,2,3,4,5,6,7] # 1
# lis = [5,6,7,8,1,2,3,4] # 4

# Driver:
# print (find_index_of_rotation(lis))