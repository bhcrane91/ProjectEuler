fn main() {
    let mut prime = 1;
    let mut n = 0;
    while n < 10001 {
        prime += 1;
        if check_prime(prime) {n += 1};
    }
    println!("{}st prime = {}",n,prime)
}

fn check_prime(n: i32) -> bool {
    if n <= 1 {return false} ;
    if n == 2 {return true};
    if n % 2 == 0 {return false};
    let sqrt_n = (n as f64).sqrt() as i32;
    for i in (3..=sqrt_n).step_by(2) {
        if n % i == 0 {return false};
    }
    true
}


