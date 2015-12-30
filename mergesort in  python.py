lst = [3,5,7,3,1,3,2,45,78, 22, 16, 4]

def merger(left_lst, right_lst):
    if not left_lst:
        return right_lst
    if not right_lst:
        return left_lst
    if left_lst[0] <= right_lst[0]:
        return [left_lst[0]] + merger(left_lst[1:], right_lst)
    return [right_lst[0]] + merger(left_lst, right_lst[1:])


def mergersort(lis):
    if len(lis) < 2:
        return lis
    else:
        mid = len(lis) // 2
        left_list = lis[:mid]
        right_list = lis[mid:]
        pss = merger(mergersort(left_list), mergersort(right_list))
        return pss
print(lst)
print (mergersort(lst))


def space_efficient_merge(lis1, lis2, lis3):
    lis1_index = 0
    lis2_index = 0
    lis3_index = 0
    while lis1_index < len(lis1) and lis2_index < len(lis2) and lis3_index < len(lis3):
        if lis1[lis1_index] < lis2[lis2_index]:
            lis3[lis3_index] = lis1[lis1_index]
            lis1_index += 1
        elif lis2[lis2_index] <= lis1[lis1_index]:
            lis3[lis3_index] = lis2[lis2_index]
            lis2_index += 1
        lis3_index += 1
    # checking for leftovers
    while lis1_index < len(lis1):
        lis3[lis3_index] = lis1[lis1_index]
        lis3_index += 1
        lis1_index += 1
    while lis2_index < len(lis2):
        lis3[lis3_index] = lis2[lis2_index]
        lis2_index += 1
        lis3_index += 1