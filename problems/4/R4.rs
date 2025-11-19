fn main() {
    let digits = 3;
    let bot = 10_i32.pow(digits - 1);
    let top = 10_i32.pow(digits);
    let mut max = [0, 0, 0];

    for i in (bot..top).rev() {
        for j in (bot..=i).rev() {
            let p = i * j;
            let str_p = p.to_string();
            if p > max[0] && check_palindrome(&str_p) {
                max[0] = p;
                max[1] = i;
                max[2] = j;
            }
        }
    }

    println!("Max: {} | Factors: ({},{})", max[0], max[1], max[2]);
}

fn check_palindrome(s: &str) -> bool {
    let bytes = s.as_bytes();
    for i in 0..(bytes.len() / 2) {
        if bytes[i] != bytes[bytes.len() - i - 1] {
            return false;
        }
    }
    true
}
