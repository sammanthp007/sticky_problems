def balanced_paranthesis(string):
    opening_brackets = {'(' : ')', '{' : '}', '[' : ']'}
    closing_brackets = {')','}', ']'}
    stack = []
    for i in string:
        # case 1 when it is opening bracket -> add it to a stack
        if i in opening_brackets:
            stack.append(i)
        # case 2 when it is a closing bracket -> pop out from the stack and see if it matches
        elif i in closing_brackets:
            if len(stack) == 0:
                return False
            opening = stack.pop()
            if opening_brackets[opening] != i:
                return False
    return not bool(len(stack))

s = '[([])]'
print (balanced_paranthesis(s))
