# Problem: given n, find the number of different ways to write
# n as the sum of 1, 3, 4


# input: a number that is to be achieved by addition of 1 3 and/or 4
# output: an integer denoting the number of ways the sum1 can be achieved from 1, 3, 4
# working: 
def sum_of_1_3_4(sum1):
    if sum1 <= 0:
        return 0
    elif sum1 == 1:
        return 1
    elif sum1 == 2:
        return 1
    elif sum1 == 3:
        return 2
    elif sum1 == 4:
        return 4
    else:
        return sum_of_1_3_4(sum1 - 1) + sum_of_1_3_4(sum1 - 3) + sum_of_1_3_4(sum1 - 4)
    
print(sum_of_1_3_4(5))
print (sum_of_1_3_4(4) + sum_of_1_3_4(2) + sum_of_1_3_4(1))