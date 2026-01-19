fn main() {
    let limit = 2000000;
    let mut ans: u128 = 2;
    let mut num_primes = 1;
    for i in (1..limit).step_by(2) {
        if is_prime(i) {
            ans += i as u128;
            num_primes += 1;
        }
    }
    println!("Number of Primes below {}: {} | Sum: {}", limit, num_primes, ans);
}

fn is_prime(n: i32) -> bool {
    if n <= 1 {
        return false;
    }
    if n == 2 {
        return true;
    }
    if n % 2 == 0 {
        return false;
    }

    let limit = (n as f64).sqrt() as i32; 
    for i in (3..limit+1).step_by(2) { 
        if n % i == 0 {
            return false;
        }
    }
    return true
}