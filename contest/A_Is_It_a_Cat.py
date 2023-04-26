from collections import defaultdict
test = int(input())

for _ in range(test):
    n = int(input())
    string = input()
    arr = 'meow'
    answer = ''
    for i in range(n):
        temp = string[i].lower()
        if not answer:
            answer += temp
        elif answer and temp != answer[-1]:
            answer += temp
    if answer == arr:
        print("YES")
    else:
        print("NO")    



