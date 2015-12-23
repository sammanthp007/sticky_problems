# class Solution:
#     # @param A : list of integers
#     # @param B : integer
#     # @return an integer
#     def coinchange2(self, A, B):
#         A.sort()
#         self.ways = 0
#         self.ways += self.coin_change(A, B, len(A) - 1)
#         return self.ways
        
#     def coin_change(self, lis, sum1, index):
#         # base cases
#         if sum1 == 0:
#             return 1
#         if sum1 < 0:
#             return 0
#         if sum1 > 0 and index <= 0:
#             return 0
#         # case : when the sum is cosiderable
#         return self.coin_change(lis, sum1 - lis[index - 1], index) + self.coin_change(lis, sum1, index - 1)

# a = Solution()
# lis = [ 18, 24, 23, 10, 16, 19, 2, 9, 5, 12, 17, 3, 28, 29, 4, 13, 15, 8 ]
# sum1 =  458
# print (a.coinchange2(lis, sum1))

