F = [1]
for i in range(1,10):
    F.append(F[i-1]*i)

def dig_fac(n):
    s = 0
    while n > 0:
        s += F[n%10]
        n //= 10
    return s 

next_int = {}
ans = 0
N = 1000000
L = 60

for n in range(N):
    seq = set([n])
    curr_term = n
    next_term = dig_fac(n)
    while next_term not in seq:
        seq.add(next_term)
        next_int[curr_term] = next_term
        curr_term = next_term
        next_term = next_int.get(curr_term,None)
        if next_term is None:
            next_term = dig_fac(curr_term)


    if len(seq) == L:
        ans += 1

print(ans)