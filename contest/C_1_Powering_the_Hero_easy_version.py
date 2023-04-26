test = int(input())
for _ in range(test):
    n = int(input())
    arr = list(map(int,input().split()))
    bones = []
    i = hero = 0
    stack = []
    while i < len(arr):
        if bones and arr[i] == 0:
            hero += bones.pop()
        elif bones and arr[i] > 0:
            while bones and arr[i] < bones[-1]:
                stack.append(bones.pop())
            bones.append(arr[i])  
            while stack:
                bones.append(stack.pop())
        elif not bones and arr[i] > 0:
            bones.append(arr)
        i += 1

    print(hero)


