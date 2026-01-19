function sum_even_fibs(arg::Int)
    a = 0
    b = 1 
    sum = 0
    while b < arg
        tmp = b
        b += a 
        a = tmp 
        if b % 2 == 0
            sum += b 
        end 
    end 
    println("Sum of even-valued Fibonacci terms < $arg: $sum")  
end 

arg = 4000000
sum_even_fibs(arg)