def permutation_of_string(string):
    # take the last characte of the string, chopp it off and find the pemutation of the string without the last string. 
    # Then put the last string in all positions of the smaller words permutation.
    # the output
    result = []
    if len(string) == 0:
        return
    if len(string) == 1:
        return [string]
    # chop off the last character
    last = string[-1]
    # find the permutation of the smaller string
    perms = permutation_of_string(string[:-1])
    # put the last character in every place
    for words in perms:
        for index in range(len(words) + 1):
            result.append(words[:index] + last + words[index:])
    return result


p = permutation_of_string("saur")
print (p, len(p))