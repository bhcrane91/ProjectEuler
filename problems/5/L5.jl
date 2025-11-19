function gcd(a::Int, b::Int)
    while b != 0
        tmp = b 
        b = a % b 
        a = tmp
    end
    return a
end

function lcm(a::Int,b::Int)
    return div(a*b, gcd(a,b))
end

global multiple = Int64(1)
for i = 2:20
    global multiple = lcm(multiple,i)
end 

println("$multiple")