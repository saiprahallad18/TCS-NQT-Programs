stack1 = []
stack2 = []

def enqueue(x):
    stack1.append(x)

def dequeue():

    if len(stack2) == 0:
        while len(stack1) > 0:
            stack2.append(stack1.pop())

    if len(stack2) == 0:
        return "Empty"

    return stack2.pop()
enqueue(1)
enqueue(2)
enqueue(3)

print("Dequeue returns", dequeue())