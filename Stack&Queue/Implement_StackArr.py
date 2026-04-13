stack = []
top = -1
# push operation
def push(x):
    global top
    stack.append(x)
    top += 1

# pop operation
def pop():
    global top
    if top == -1:
        print("Underflow")
    else:
        value = stack[top]
        stack.pop()
        top -= 1
        return value

# peek operation
def peek():
    if top == -1:
        return "Empty"
    return stack[top]
push(1)
push(2)
push(3)

print("Pop:", pop())
print("Peek:", peek())