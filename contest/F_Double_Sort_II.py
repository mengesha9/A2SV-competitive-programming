# F. Double Sort II
# time limit per test2 seconds
# memory limit per test512 megabytes
# inputstandard input
# outputstandard output
# You are given two permutations a and b, both of size n. A permutation of size n is an array of n elements, where each integer from 1 to n appears exactly once. The elements in each permutation are indexed from 1 to n.

# You can perform the following operation any number of times:

# choose an integer i from 1 to n
# let x be the integer such that ax = i. Swap ai with ax
# let y be the integer such that by = i. Swap bi with by.
# Your goal is to make both permutations sorted in ascending order(i. e. the conditions a1 < a2 <⋯<an and b1 < b2 <⋯<bn must be satisfied) using minimum number of operations. Note that both permutations must be sorted after you perform the sequence of operations you have chosen.

# Input
# The first line contains one integer n(2≤n≤3000).

# The second line contains n integers a1, a2, …, an(1≤ai≤n
#                                                   all ai are distinct).

# The third line contains n integers b1, b2, …, bn(1≤bi≤n
#                                                  all bi are distinct).

# Output
# First, print one integer k(0≤k≤2n) — the minimum number of operations required to sort both permutations. Note that it can be shown that 2n operations are always enough.

# Then, print k integers op1, op2, …, opk(1≤opj≤n), where opj is the value of i you choose during the j-th operation.

# If there are multiple answers, print any of them.


