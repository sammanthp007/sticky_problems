# input -> an unsorted list
# output -> another unsorted list
# working -> 
#input_list ->[3,4,4,6,4,7] 
#res -> [3, 4, 6, 7] -> len(res) = m
# Big O → n * n

def remove_duplicate(lis):
    res_lis = []
    for each in lis:
        if each in res_lis:
            continue
        else:
            res_lis.append(each)
    return res_lis

# test case:
# one list with 5 items, three are repeated
# a list with three different items repeated
# empty list
# if all the items are equal
# list inside the given lis

# lis = [3,4,5,4,4]
# lis = [3,3,3]
# lis = []
print (remove_duplicate(lis))