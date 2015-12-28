# The brute force would be to contruct a lost of all powersets of A. Then using a random number generator, generate a random number from 0 to 1, and use the random 0 or 1, as the bit of a number that lies in between the number of elements and zero ([0, len(lis)]) and pick that subset. 
# We are given lis, k.
# list them in a dictionary such that the keys are the lengths of the dictionary, and the subsets are the values.

# store only one thing extra, which should probably be a number/index.
# use a random generator at max once during a function call

# requirement:
# it should be inorder.
# working:
#     we can get a random number.
#     get me the item at this position -> r,
#     then I can swap the item at r with k
#     k = k -1
# while k > 0
# return lis[len(lis) - k :] # len(lis) = 5; k = 3; lis[2:] -< 3 items

import random

def get_random_subset(lis, k):
    last_looking_index = len(lis) - 1
    siz = k
    while k > 0:
        random_index = random.randint(0, last_looking_index)
        swap(lis, last_looking_index, random_index)
        k -= 1
        last_looking_index -= 1
    return lis[len(lis) - siz:] # 5, 3, 

def swap(lis, a, b):
    lis[a], lis[b] = lis[b] , lis[a]

lis = [3,6,2,1,7,9,77]
print (get_random_subset(lis, 3))