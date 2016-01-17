# input: an integer
# output: an integer that denotes the number of 1 bits in its binary representation
class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        bit ={}
        bit[0] = 0
        bit[1] = 0
        while True:
            if A == 1:
                bit[1] += 1
                return bit[1]
            if A % 2 == 0:
                A = A / 2
                bit[0] += 1
            else:
                A = A // 2
                bit[1] += 1


# This is a faster solution
# It makes use of the fact that A & A - 1 will unset the least significant 1 from A 
class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        res = 0
        while A > 0:
            A ^= A & (~(A - 1))
            res += 1
        return res