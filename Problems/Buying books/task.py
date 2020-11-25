from _collections import deque

n = int(input())
tasks = [[x for x in input().split(" ", 1)] for _i in range(n)]
stack = deque()
result = ""
for elem in tasks:
    if elem[0] == "BUY":
        stack.append(elem[1])
    elif elem[0] == "READ":
        result += stack.pop() + "\n"
print(result)
