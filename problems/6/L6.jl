function main()
    n = 100
    sum_of_squares = div((n * (n+1) * (2*n + 1)), 6)
    square_of_sums = div((n * (n+1)), 2)
    square_of_sums *= square_of_sums
    println("L -> : $(square_of_sums-sum_of_squares)")
end

main()