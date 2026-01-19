fn main() {
    let target = 500;
    let mut tri = 1;
    let mut itr = 1;
    let mut div = 1;
    while div < target {
        itr += 1;
        tri += itr; 
        div = 0;
        let sqrt_n = (tri as f64).sqrt() as i32;
        for i in 1..sqrt_n {
            if tri % i == 0 {
                if tri / i == i {
                    div += 1;
                } else {
                    div += 2;
                }
            }
        }
    }
    println!("Triangle Number ({}): {} | Divisors: {}",itr,tri,div);
}