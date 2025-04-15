// use std::env;

fn main() {
    // let args: Vec<String> = env::args().collect();
    // let arg: i32 = args[1].parse().expect("Please provide a valid number");
    let arg: i32 = 1000;
    let mut ans = 0;

    for i in 0..arg {
        if i % 5 == 0 || i % 3 == 0 {
            ans += i;
        }
    }

    println!("Sum of multiples of 3 or 5 below {}: {}", arg, ans);
}
