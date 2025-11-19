fn main() {
    let t = 3;
    let b = 7;
    let d = 1_000_000;
    let mut diff = f64::INFINITY;
    let mut up_j = 0;
    let mut up_i = 0;

    for i in 1..=d {
        let x = (3 * i) / 7;
        for j in 1..=x {
            let s = (t as f64 / b as f64) - (j as f64 / i as f64);
            if s < diff && s != 0.0 {
                diff = s;
                up_i = i;
                up_j = j;
            }
        }
    }

    println!("{diff} {up_j} {up_i}");
}
