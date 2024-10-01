function prime_factors(n::Int)
    factors = []
    num = n
    while n % 2 == 0
        push!(factors,2)
        n /= 2
    end 

    for i = 3:2:round(Int,sqrt(n))+1
        while n % i == 0
            push!(factors, i)
            n /= i 
        end 
    end 
    if n > 1
        push!(factors,round(Int,n))
    end
    println("Julia -> Prime Factors of $num: [$(join(factors," "))] | Largest -> $(factors[end])")
end 

prime_factors(600851475143)