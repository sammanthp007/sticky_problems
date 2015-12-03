
def longestCommonPrefix(A):
    longest_word_size = len(A[0])
    longest_word = A[0]
    if len(A) < 1:
        return None
    longest_common_prefix = ''
    temp_letter = longest_common_prefix
    for index in xrange(len(A[0])):
        for word in A:
            temp_letter = A[0][index]
            if not both_same(temp_letter, word[index]):
                return longest_common_prefix
        longest_common_prefix += word[index]
    return longest_common_prefix

        
def both_same(same, a):
    if same == a:
        return True
    return False

lis = [ "abcd", "abcd", "abfgh" ]

print (longestCommonPrefix(lis))