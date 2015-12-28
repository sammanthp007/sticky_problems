# Given a word containing a set of words separated by white space, we would like to transform it to a string in which the words appear in the reverse order. For example, "Alice likes Bob" transforms to "Bob likes Alice". We do not need to keep the original string.

# Implement a function for reversing the words in a string s. Your function should use O(1) space.

def reverse_word(sentence):
    # Phase1: traverse to get where the words are
    letter_ptr = 0
    word_starts = [0]
    word_length =[]
    word_begin = 0
    while letter_ptr < len(sentence):
        while letter_ptr < len(sentence) and sentence[letter_ptr] != ' ':
            letter_ptr += 1
        temp_length = letter_ptr - word_begin
        word_length.append(temp_length)
        letter_ptr += 1
        word_starts.append(letter_ptr)
        word_begin = letter_ptr
    # Phase2: reverse the sentence based on words, words are determined by spaces in between
    res = ''
    for i in range(len(word_length)):
        res = sentence[word_starts[i]: word_starts[i] + word_length[i]] + ' ' + res
    return res
    
sen = "Bob likes alice"
print(reverse_word(sen))