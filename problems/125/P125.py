B = 10**8

sum_of_squares = lambda n: (n * (n+1) * (2*n + 1)) // 6
consecutive = lambda a,b: sum_of_squares(b) - sum_of_squares(a-1)
def is_palindrome(n):
    # if n[-1] == "0":
    #     n = "0" + n
    for i in range(len(n)//2):
        if n[i] != n[len(n)-1-i]:
            return False
    return True

N = 7071
S = 0
k = 0
a = set()
for i in range(1,N):
    for j in range(i-1,0,-1):
        c = consecutive(j,i)
        if c >= B:
            break 
        s = str(c)
        if is_palindrome(s) and c not in a:
            k += 1
            S += c 
            a.add(c)
            # print(k,":",j,i,c,S,(c < B))
# do with prefix sum because faster
print(S)
