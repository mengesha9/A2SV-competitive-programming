l = int(input())

x = 0
stack = [1]
for _ in range(l):
    command = input().split()
    if command[0] == 'end':
        stack.append(command[0])
    if stack and len(command)==2:
        stack.append(int(command[1]))
    if command[0] == 'add':

        while stack and stack[-1] != 'end':
            if x == 0:
                x += stack.pop()
            else:
                x *=stack.pop()

if x > (2**32)-1:
    print("OVERFLOW!!!")
else:
    print(x)









