class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        length = 0
        if len(A) == 0:
            return 0
        for letter_index in range(len(A)):
            if A[letter_index] == ' ':
                if (letter_index < len(A) - 1) and A[letter + 1] != ' ':
                    length = 0
            else:
                length += 1
        return length
    # def lengthOfLastWord(self, A):
    #     after_letters = False
    #     if len(A) == 0:
    #         return 0
    #     length = 0
    #     for letter in A[::-1]:
    #         if letter == ' ' and after_letters:
    #             return length
    #         if letter == ' ' and not after_letters:
    #             continue
    #         length += 1
    #         after_letters = True
    #     return length
