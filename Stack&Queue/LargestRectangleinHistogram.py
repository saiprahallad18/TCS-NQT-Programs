heights = [2,1,5,6,2,3]
stack = []
max_area = 0
i = 0
n = len(heights)

while i < n:
    if len(stack) == 0 or heights[stack[-1]] <= heights[i]:
        stack.append(i)
        i += 1
    else:
        top = stack.pop()
        if len(stack) == 0:
            area = heights[top] * i
        else:
            area = heights[top] * (i - stack[-1] - 1)
        if area > max_area:
            max_area = area

while len(stack) > 0:
    top = stack.pop()
    if len(stack) == 0:
        area = heights[top] * i
    else:
        area = heights[top] * (i - stack[-1] - 1)
    if area > max_area:
        max_area = area

print(max_area)