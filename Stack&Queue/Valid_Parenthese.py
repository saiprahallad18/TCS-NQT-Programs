s = "{[()]}"
stack = []
valid = True

for ch in s:
    if ch == '(' or ch == '{' or ch == '[':
        stack.append(ch)
    else:
        if len(stack) == 0:
            valid = False
            break
        top = stack.pop()
        if ch == ')' and top != '(':
            valid = False
        if ch == '}' and top != '{':
            valid = False
        if ch == ']' and top != '[':
            valid = False

if len(stack) != 0:
    valid = False
print(valid)