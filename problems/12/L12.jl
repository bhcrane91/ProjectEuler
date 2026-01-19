function main()
    target = 500
    tri = 1
    itr = 1 
    divs = 1 
    sum = 0
    while divs < target 
        itr += 1
        tri += itr 
        divs = 0
        sum = 0
        for i in 1:ceil(Int, sqrt(tri))
            if tri % i == 0
                if tri / i == i 
                    divs += 1 
                else 
                    divs += 2 
                    sum += (tri/i)
                end
                sum += i
            end
        end
    end
    print("Triangle Number ($(itr)): $(tri) | Divisors: $(divs)")
end

main()