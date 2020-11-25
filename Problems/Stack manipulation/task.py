from _collections import deque

n = int(input())
tasks = [[x for x in input().split()] for _i in range(n)]
stack = deque()
for elem in tasks:
    command = elem[0]
    if command == "PUSH":
        stack.append(int(elem[1]))
    elif command == "POP":
        stack.pop()
for _i in range(len(stack)):
    print(stack.pop())
