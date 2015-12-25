# Five hundred closed doors along a corridor are numbered from 1 to 500. A person walks through the corridor and opens each door. Another person walks through the corridor and closes every alternate door. Continuing in this manner, the ith person comes and toggles the position of every i-th door starting from door i.

# iteration: 1
# all odd people are going to open
# all even people are going to close

# 0 0 0 0 0 0 0 0 0 0 <- all closed

# 1 1 1 1 1 1 1 1 1 1 --odd(1)  
# 1 0 1 0 1 0 1 0 1 0 --even(2) 
# 1 0 0 0 1 1 1 0 0 0
# 1 0 0 1 1 1 1 1 0 0
# 1 0 0 1 0 1 1 1 0 1
# 1 0 0 1 0 0 1 1 0 1
# 1 0 0 1 0 0 0 1 0 1
# 1 0 0 1 0 0 0 0 0 1
# 1 0 0 1 0 0 0 0 1 1
# 1 0 0 1 0 0 0 0 1 0

# prime numbers are all closing down
# if a num has even number of divisors, then he closes -> you do not have a square root
# if a num has odd number of divisors, then he opens -> you do have a square root -> all the square numbers are open

def is_open(nth):
    res = []
    for i in range(1, nth):
        sqr = i * i
        if sqr > nth:
            break
        res.append(sqr)
    return res

print (is_open(40))