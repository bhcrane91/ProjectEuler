fn main() {
    let mut my_lcm: i64 = 1;
    for i in 1..20 {
        my_lcm = lcm(my_lcm, i);
    }
    println!("{}",my_lcm);
}

fn gcd(mut a:i64, mut b:i64) -> i64 {
    while b != 0 {
        let tmp: i64 = b;
        b = a % b;
        a = tmp;
    }
    return a;
}

fn lcm(a:i64,b:i64) -> i64 {
    let mult = a*b;
    return mult.div_euclid(gcd(a,b));
}