fn main() {
    let mut factors = vec![];
    let num = 600851475143;
    let mut n: i64 = num;
    while n % 2 == 0 {
        factors.push(2);
        n /= 2;
    }
    for i in (3..((n as f64).sqrt() as i64)+1).step_by(2) {
        while n % i == 0 {
            factors.push(i);
            n /= i;
        }
    }
    if n > 1 {
        factors.push(n);
    }
    
    print!("Prime Factors of {}: ",num);
    for factor in &factors {
        print!("{} ",factor);
    }
    print!("| Largest -> {}", factors[factors.len()-1]);
    println!("")
}