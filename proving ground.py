def mergesort(lis):
    if len(lis) == 1:
        return lis
    elif len(lis) == 0:
        return
    else:
        a = merger(mergesort(lis[:len(lis)//2]), mergesort(lis[len(lis)//2:]), lis)
        return lis

def merge(lis1, lis2):
    if len(lis1) == 0:
        return lis2
    elif len(lis2) == 0:
        return lis1
    elif lis1[0] < lis2[0]:
        return [lis1[0]] + merge(lis1[1:], lis2)
    else:
        return [lis2[0]] + merge(lis1,lis2[1:])

def merger(lis1, lis2, lis3):
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

lis = [3,2,1,5,24,1,55,0,-1,7,34,6,3]
print (mergesort(lis))