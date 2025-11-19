function main()
    digits = 3
    bot = 10^(digits - 1)
    top = 10^digits
    max = [0, 0, 0]

    for i in top:-1:bot
        for j in i:-1:bot
            p = i * j
            str_p = string(p)
            if p > max[1] && check_palindrome(str_p)
                max[1] = p
                max[2] = i
                max[3] = j
            end
        end
    end

    println("Max: $(max[1]) | Factors: ($(max[2]),$(max[3]))")
end

function check_palindrome(s::String)
    return s == reverse(s)
end

main()
