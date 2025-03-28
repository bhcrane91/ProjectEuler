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
    for i = 3:2:round(Int,sqrt(n))+1
        if n % i == 0
            return false
        end 
    end 
    return true
end 

function main() 
    limit = 10
    ans = 0
    num_p = 0
    for i = 1:limit 
        if is_prime(i)
            ans += i 
            num_p += 1
            print("$i ")
        end 
    end
    println("L -> Number of Primes below $limit: $num_p | Sum: $ans")
end

main()