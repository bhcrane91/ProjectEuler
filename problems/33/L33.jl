function gcd(a,b)
    while b != 0
        t = b 
        b = a % b 
        a = t 
    end 
    return a 
end

function main()
    a = 1 
    b = 1
    for i in 1:10
        for j in 1:10
            n = (i * 10) + j 
            for k in 9:-1:-1
                m = (j * 10) + k
                if k*n == m*i
                    a *= i
                    b *= k 
                    println("$(n) $(m)")
                end 
            end
        end 
    end
    g = gcd(a,b)
    while g != 1
        a /= g 
        b /= g 
        g = gcd(a,b)
    end 
    println("$(a) $(b)")
end

main()