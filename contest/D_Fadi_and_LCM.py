import math


def lcm(a, b):
    return (a*b) // math.gcd(a, b)


def main():
    x = int(input())

    a = 1
    b = x

    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            if lcm(i, x//i) == x:
                if max(i, x//i) < max(a, b):
                    a = i
                    b = x//i

    print("{} {}".format(a, b))


main()
