# Write a function which takes as input a phone number, specified as a string of digits, return all possible character sequences that correspond to the phone number. The cell phone keypad is specified by a mapping M that takes a digit and returns the corresponding set of characters. The character sequences do not have to be legal words or phrases.

# My original approach
num_equivalent = {2 : ['A','B', 'C'], 3 : ['D', 'E', 'F'], 4 : ['G','H','I'], 5 : ['J', 'K', 'L'],
                 6: ['M', 'N', 'O'], 7: ['P', 'Q', 'R', 'S'], 8: ['T', 'U', 'V'], 9: ['W', 'X','Y', 'Z']}


def get_phone_pnemonic(num, lis):
    temp_num = str(num)
    # print (num)
    if num == None:
        return lis
    if len(lis) == 0:
        current_num = int(temp_num[0])
        lis.append(num_equivalent[current_num][0])
        lis.append(num_equivalent[current_num][1])
        lis.append(num_equivalent[current_num][2])
        lis = get_phone_pnemonic(int(temp_num[1:]), lis)
        return lis
    if len(temp_num) == 1:
        length = len(lis)
        for index in range(length):
            incomplete = lis.pop(index)
            comp0 = incomplete + num_equivalent[num][0]
            lis = [comp0] + lis
            comp1 = incomplete + num_equivalent[num][1]
            lis.append(comp1)
            comp2 = incomplete + num_equivalent[num][2]
            lis.append(comp2)
        return lis
    else:
        length = len(lis)
        current_num = int(temp_num[0])
        for index in range(length):
            incomplete = lis.pop(index)
            comp0 = incomplete + num_equivalent[current_num][0]
            lis = [comp0] + lis
            comp1 = incomplete + num_equivalent[current_num][1]
            lis.append(comp1)
            comp2 = incomplete + num_equivalent[current_num][2]
            lis.append(comp2)
        lis = get_phone_pnemonic(int(temp_num[1:]), lis)
        return lis
            
lis = []
print (get_phone_pnemonic(234, lis))
# <<<<<<<<<<<<<<<<<<<<<<<<< end of original approach >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# shorter solution, similar approach:

keyboard = {
  '1': [],
  '2': ['a','b','c'],
  '3': ['d','e','f'],
  '4': ['g','h','i'],
  '5': ['j','k','l'],
  '6': ['m','n','o'],
  '7': ['p','q','r','s'],
  '8': ['t','u','v'],
  '9': ['w','x','y','z'],
  '0': []
}
 
lis = []
def printkeys(numbers, prefix=""):
    if len(numbers)==0:
        lis.append(prefix)
        return
 
    for letter in keyboard[numbers[0]]:
        printkeys(numbers[1:], prefix+letter)
 
printkeys("234")
print (lis)    