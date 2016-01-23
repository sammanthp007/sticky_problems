# here , from the question,
# two lists
# of numbers
# both sorted

# input -> two sorted lists
# output -> a list that is sorted
# working -> 
# Have three pointers, one pointing to lis1[0], another pointing to lis2[0]
# need a final list
# compare, and append the smaller one to the final, and increase the pointer for that lis


def merge(lis1, lis2):
    i = 0
    j = 0
    res_lis = []
    if len(lis1) == 0:
        return lis2
    if len(lis2) == 0:
        return lis1
    while len(res_lis) < len(lis1) + len(lis2):
        if i == len(lis1):
            res_lis.extend(lis2[j:])
            break
        elif j == len(lis2):
            print ('here')
            res_lis.extend(lis1[i:])
            break
        elif i < len(lis1) and j < len(lis2):
            if lis1[i] <= lis2[j]:
                res_lis.append(lis1[i])
                i += 1
            else:
                res_lis.append(lis2[j])
                j += 1
    return res_lis


# i = 0
# j = 0

# [2,4,6,8], [1,3,5,7]
# [], []
# [3,4,5,6,6,6],[2,6,6,6,7,8]
lis1 = [-5,-3,-1]
lis2 = [-5,-4,-2]
# [1,2,3,4],[1,2,3,4]
# [-1,-3,-5], [-2,-4, -5]
print (merge(lis1, lis2))