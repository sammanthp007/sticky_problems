# implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

# with additional data structures
def unique_char(string):
    dic = {}
    for letter in string:
        if letter in dic:
            return False
        dic[letter] = 1
    return True

def has_unique_char(string):
    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            if string[i] == string[j]:
                return False
    return True

string = 'setgn'
# print(has_unique_char(string))

def isUniqueChars(string):
  checker = 0
  for c in string:
    val = ord(c) - ord('a')
    if (checker & (1 << val) > 0):
      return False
    else:
      checker |= (1 << val)
  return True