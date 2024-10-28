fn main() {
    let mut my_lcm: i64 = 1;
    for i in (1..20) {
        my_lcm = lcm(my_lcm, i);
    }
    System.out.println(my_lcm);
}

fn prime_factors(n:i64) {
    if n <= 1 {
        return vec![];
    }
    let mut factors = vec![];
    while n % 2 == 0 {
        push!(factors, n);
        n /= 2;
    }
    for i in (3..(10i32.sqrt(n)+1)).step_by(2) {
        while n % i == 0 {
            push!(factors, i);
            n /= i;
        }
    }
    if n > 1 {
        push!(factors, n)
    }
    return factors
}

fn gcd(a:i64,b:i64) {
    let pfa = prime_factors(a);
    let mut pfb = prime_factors(b);
    let mut div: i64 = 1;
    for n in pfa {
        if n in pfb {
            div *= n;
            pfb.pop(n);
        }
    }
    return div;
}

fn lcm(a:i64,b:i64) -> i64 {
    return (a*b).div_euclid(gcd(a,b));
}