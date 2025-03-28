function main()
    for a in 100:1000 
        for b in (a):(1000-a)
            c = 1000-a-b
            if c^2==a^2+b^2
                print("L -> Triple: ($(a),$(b),$(c)) | Product: $(a*b*c)")
                return
            end
        end
    end
end 

main()