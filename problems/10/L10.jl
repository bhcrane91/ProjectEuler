function is_prime(n::Int)
    if n <= 1
        return false
    end 
    if n == 2
        return true
    end 
    if n % 2 == 0
        return false
    end 
    for i = 3:2:floor(Int,sqrt(n))+1
        if n % i == 0
            return false
        end 
    end 
    return true
end 

function main() 
    limit = 2000000
    ans = 2
    num_p = 1
    for i = 1:2:limit
        if is_prime(i)
            ans += i 
            num_p += 1
        end 
    end
    println("Number of Primes below $limit: $num_p | Sum: $ans")
end

main()