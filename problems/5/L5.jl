function prime_factors(n::Int)
    if n <= 1
        return []
    end 
    factors = []
    while n % 2 == 0
        push!(factors,2)
        n //= 2
    end 
    for i = 3:2:round(Int,sqrt(n))+1
        while n % i == 0
            push!(factors,i)
            n //= i 
        end 
    end 
    if n > 1
        push!(factors,round(Int,n))
    end 
    return factors
end 

function gcd(a::Int,b::Int)
    prime_factors_a = prime_factors(a)
    prime_factors_b = prime_factors(b)
    div = 1
    for n = prime_factors_a
        if div in prime_factors_b
            div *= n 
            deleteat!(prime_factors_b, findfirst(x -> x == n, prime_factors_b))
        end 
    end
    return Int(div)
end 

function lcm(a::Int,b::Int)
    return a*b//gcd(a,b)
end

global multiple = Int64(1)
for i = 2:20
   global multiple = lcm(multiple,i)
end 

println(multiple)