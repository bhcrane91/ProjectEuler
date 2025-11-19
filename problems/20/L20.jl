function main()
    n = 100
    println("Sum of digits of $(n)! = $(sum(digits(factorial(big(n)))))")
end

main()