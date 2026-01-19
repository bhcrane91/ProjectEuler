fn main() {
    let target = 1000000;
    let mut max: u64 = 0;
    let mut num: u64 = 0;
    for i in 1..target {
        let mut itr: u64 = 1;
        let mut x: u64 = i;
        while x != 1 {
            if x % 2 == 0 {
                x /= 2;
            } else {
                x = 3*x + 1;
            }
            itr += 1;
        }
        if itr > max {
            max = itr;
            num = i;
        }
    }
    println!("Maximum Collatz Sequence for c[0] < {}: c[0] = {} | Length: {}",target,num,max);
}