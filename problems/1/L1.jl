function sum_of_multiples(arg::Int)
    ans = 0
    for i in 0:(arg - 1)
        if i % 5 == 0 || i % 3 == 0
            ans += i
        end
    end
    println("Julia: Sum of multiples of 3 or 5 below $arg: $ans")
end

# Get the command line argument
# arg = parse(Int, ARGS[1])
arg = 1000
sum_of_multiples(arg)
