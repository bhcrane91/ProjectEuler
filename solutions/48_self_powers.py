sum = 0
for i in range(1,1001):
    sum += pow(i,i)
print(sum % (10**10))