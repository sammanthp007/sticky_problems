def merge_two_list(lis1, lis2):
    index1 = 0
    index2 = 0
    lis3 = []
    while index1 < len(lis1) or index2 < len(lis2):
        if index1 < len(lis1) and index2 < len(lis2):
            if lis1[index1] <= lis2[index2]:
                lis3.append(lis1[index1])
                index1 += 1
            else:
                lis3.append(lis2[index2])
                index2 += 1
        elif index1 < len(lis1):
            lis3.append(lis1[index1])
            index1 += 1
        elif index2 < len(lis2):
            lis3.append(lis2[index2])
            index2 += 1
    return lis3

lis1 = [1,3,5,7,9]
print (merge_two_list(lis1, lis1))