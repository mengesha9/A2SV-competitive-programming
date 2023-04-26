import math

x = int(input())

# We can get to x by doubling 1 log2(x) times.
num_bacteria_added = int(math.log2(x))

print(num_bacteria_added + 1)
