from _collections import deque


n = input()
stack = deque()
error = False
for elem in n:
    if elem == "(":
        stack.append("(")
    elif elem == ")":
        if len(stack) != 0:
            stack.pop()
        else:
            error = True
            break
if len(stack) != 0 or error:
    print('ERROR')
else:
    print('OK')
