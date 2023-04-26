
def S(num):
    st = str(num)
    total = 0
    for i in range(len(st)):
        total += int(st[i])
    return total

n = int(input())
answer = 0
if n < 10:
    print(n)
else:
    l = len(str(n))-1
    total = 0
    num = ''
    for i in range(l):
        num += '9'
        total += 9
    b= n - int(num)
    answer = S(b)  + total   

    print(answer)



