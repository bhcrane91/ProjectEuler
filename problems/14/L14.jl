function collatz(n)
    i = 1
    x = n 
    while x != 1
        if x % 2 == 0
            x /= 2
        else
            x = 3*x + 1
        end 
        i += 1
    end
    return i, n
end 

function main() 
    max = 0
    num = 0
    t = 1000000
    for i in 1:t
        curr, cn = collatz(i)
        if curr > max
            max = curr 
            num = cn 
        end 
    end 
    print("Maximum Collatz Sequence for c[0] < $(t): c[0] = $(num) | Length: $(max)\n")
end

main()