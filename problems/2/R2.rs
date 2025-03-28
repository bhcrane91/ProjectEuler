fn main() {
    let mut a = 0;
    let mut b = 1;
    let mut sum = 0;
    let target: i32 = 4000000;
    while b < target {
        let tmp = b;
        b += a;
        a = tmp;
        if b % 2 == 0 { 
            sum += b;
        }
    }
    println!("Rust: Sum of even-valued Fibonacci terms < {}: {}", target, sum);
}