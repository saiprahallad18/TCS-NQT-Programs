exp = ["2","3","1","*","+","9","-"]
stack = []

for token in exp:
    if token.isdigit():
        stack.append(int(token))

    else:
        b = stack.pop()
        a = stack.pop()

        if token == '+':
            stack.append(a + b)

        elif token == '-':
            stack.append(a - b)

        elif token == '*':
            stack.append(a * b)

        elif token == '/':
            stack.append(a // b)

print(stack[0])