
def find(l,r):
    tmpl = l.bit_length()
    tmp = r.bit_length()
    if tmpl != tmp:
        return (2 ** (tmp-1)) ^ ((2 ** (tmp-1)-1))
    
    return find(l-2**(tmpl-1), r-2**(tmpl-1))


l, r = map(int,input().split())
if l == r:
    print(0)
else:    
    print(find(l,r))
