# # Pythonic way -> costs a lot of space O(n ** 3)
# def merge(lisA, lisB):
#     if not lisA and not lisB:
#         return
#     if not lisA:
#         return lisB
#     if not lisB:
#         return lisA
#     if lisA[0] > lisB[0]:
#         return [lisB[0]] + merge(lisA, lisB[1:])
#     else:
#         return [lisA[0]] + merge(lisA[1:], lisB)

# lis1 = [3,4,5,66,77,88]
# lis2 = [6,8,9,12,454,623]
# print (merge(lis1, lis2))

# # Non-pythonic, and pointer oriented
# def merger(lisA, lisB):
#     i = 0 # pointer in A
#     j = 0 # pointer in B
#     k = 0 # pointer in A but of the position we will be looking at
#     while k != len(lisA) + len(lisB):
#         if i >= len(lisA):
            
#         if lisA[i] <= lisB[j]:
#             i += 1
#             k += 1
#         else:
#             swap(lisA, lisB, i, j)
#             i += 1
#             j += 1

# 2023295370