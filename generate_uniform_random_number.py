# Generate Uniform Random Numbers

'''How would you implement a random number generator that generates a random integer i in [a,b], given a random number generator that produces either zero of one with equal probability? All generated values should have equal probability. What is the run time of your algorithm?
'''

# input = a, b (the two margins inclusive)
# output = res, which is a random number in between a and b
# working:
import random

def zero_one_random():
    return random.randint(0,1)

# top = b - a + 1
# how to create a number from bits
# 0 to 8
# we need to repetedly range(0, top) -> create a bit -> add it to our result in the range -> 0 , top

def randomly_select(a, b):
    top = b - a + 1
    res = top + 1
    while res >= top:
        res = 0
        iterator = 1
        while iterator < top:
            bit = zero_one_random()
            res = res << 1
            res = res | bit
            iterator = iterator << 1
    return res + a

# res = {000, 001, 010, 011, 100, 101}

print (randomly_select(12, 19))