function main() 
    n = 20
    triangle = [0 for i=0:2*n]
    setindex!(triangle,1,1)
    max = 0
    for row in 1:2*n+1
        for i in 1:2*n+1
            setindex!(triangle,getindex(triangle,i+1) + getindex(triangle,((i+1)%(2*n+1))),i)
            if getindex(triangle,i) > max
                max = getindex(triangle,i)
            end
        end
    end
    println(triangle)
    println("Paths in $(n)x$(n) square: $(max)")
end 

main()