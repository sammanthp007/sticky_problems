lis = []
def permutation_string(string):
    if len(string) == 0:
        return -1
    if len(string) == 1:
        return [string]
    # for everthing else : get 
    return list(merge(string[0], permutation_string(string[1:])))

def merge(character, arr):
    array = set() # make this the same list as lis, for space complexity
    for string in arr:
        index = 0
        while index <= len(arr):
            array.add(merge_util(character, string, index)) # gives a different type of string
            index += 1
    return array
    
def merge_util(character, string, index):
    return string[:index] + character + string[index:]
    
# working:
# fis -> 3 * 2 = 6

p = permutation_string('sam')
print (p, len(p))