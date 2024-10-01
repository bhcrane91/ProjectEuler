# only nums between N and N + K * sum[j=0][log10(N)] 10**j
# will share the same number of digits

for i in range(7):
    j = (10**i + 6 * sum(10**j for j in range(i))) + 1
    for k in range(i,j):
        one = set(str(k))
        six = set(str(6*k))
        if one == six:
            nums = [k,6*k]
            for n in range(2,6):
                if set(str(n*k)) == one:
                    nums.append(n*k)
                else:
                    break 
            if len(nums) == 6:
                print(k,nums)

        
            