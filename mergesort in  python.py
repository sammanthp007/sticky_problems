lst = [3,5,7,3,1,3,2,45,78, 22, 16, 4]

def merger(left_lst, right_lst):
    i = 0
    j = 0
    res = []
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