
def powerthree(n):
    if n==1:
        return 1
    if n==0:
        return 0
    return powerthree(n-1)+powerthree(n-2)

n=10
print(powerthree(n))

print(2**31)