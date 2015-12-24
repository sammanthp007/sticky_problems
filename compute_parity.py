# the parity of a sequence of bits is 1 if the number if 1s in the sequence is odd;otherwise, it is 0. Parity checks are used to detect single bit errors in data storage and communication. It is fairly straightforward to write code that computes the parity of a single 64-bit nonnegative integer.

# How would you go about computing the parity of a very large number of 64-bit nonnegative integers?

# working
# 0000 0000 0010 0110

def no_of_ones(num):
    count = 0
    while num > 0:
        # step1: get to the least significant 1
        lsf_1 = num & (~ (num - 1))
        # step2: count it
        count += 1
        # step3: remove it
        num = num ^ lsf_1
        # step4: loop back to 1
    return count

def compute_parity(num):
    count = no_of_ones(num)
    if count % 2 == 0:
        return 0
    return 1
print (compute_parity(16))