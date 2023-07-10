test = int(input())

for _ in range(test):
    n = int(input())
    arr = list(map(int, input().split()))

    max_sum = 0
    current_sum = 0
    i = 0
    for i in range(n):
        if i == 0:
            current_sum = arr[i]
        elif arr[i] * arr[i - 1] > 0:
            current_sum = max(current_sum, arr[i])
        else:
            max_sum += current_sum
            current_sum = arr[i]

    max_sum += current_sum

    print(max_sum)
