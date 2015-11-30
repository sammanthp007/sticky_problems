class ArrayStack(object):
    def __init__(self):
        self.stack = []
        
    def push(self, d):
        self.stack.append(d)
        return True
    
    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()
    
    def top(self):
        if not self.is_empty():
            return self.stack[-1]
        return None
    
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False
    
    def size(self):
        return len(self.stack)
    
    def print_stack(self):
        print (self.stack)

greater_preference = {
    '+' : ['+', '-', '*', '/'],
    '-' : ['+', '-', '*', '/'],
    '*' : ['*', '/'],
    '/' : ['/']
}

expression = '2+4*1/2+3*2'
def infix_to_prefix(expr):
    stack = ArrayStack()
    prefix =''
    numbers = '0123456789'
    for symbol in expr:
        if symbol in numbers:
            prefix += symbol
        else:
            if stack.is_empty():
                stack.push(symbol)
            else:
                top = stack.top()
                while top in greater_preference.get(symbol, []):
                    prefix += stack.pop()
                    top = stack.top()
                stack.push(symbol)
    while not stack.is_empty():
        prefix += stack.pop()
    return prefix

# a = infix_to_prefix(expression)
# print (a)

def do_math(operator, num1, num2):
    # print (num1)
    if operator == '*':
        return num1 * num2
    elif operator == '/':
        return int(num2) / int(num1)
    elif operator == '+':
        return int(num1) + int(num2)
    elif operator == '-':
        return int(num2) - int(num1)
                
def eval_postfix(expr):
    stack = ArrayStack()
    res = 0
    for symbol in expr:
        if symbol in '0123456789':
            stack.push(int(symbol))
            stack.print_stack()
        else:
            num1 = stack.pop()
            num2 = stack.pop()
            res = do_math(symbol, num1, num2)
            stack.push(res)
            stack.print_stack()
    return stack.pop()

# b = eval_postfix(a)
# print (b)