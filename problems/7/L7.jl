function  main()
    prime = 1
    n = 0
    while n < 10001
        prime += 1
        if check_prime(prime)
            n += 1
        end 
    end 
    print("L -> $(n)st prime = $(prime)")
end

function check_prime(n::Int)::Bool
    if n <= 1
        return false
    elseif n == 2
        return true
    elseif n % 2 == 0
        return false
    end
    for i in 3:2:ceil(Int, sqrt(n))
        if n % i == 0
            return false
        end
    end
    return true
end

main()