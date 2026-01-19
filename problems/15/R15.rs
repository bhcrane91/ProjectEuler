fn main() {
    const N: usize = 20;
    let mut triangle: [u64;2*N] = [0;2*N];
    triangle[0] = 1 as u64;
    for _i in 0..(2*N) {
        for j in 0..(2*N) {
            triangle[j] += triangle[(j+1)%(2*N)];
        }
    }
    let mut max: u64 = 0;
    for pascal in &triangle {
        //println!("-> {}",*pascal);
        if *pascal > max {
            max = *pascal;
        }
    }
    println!("Paths in {}x{} square: {}",N,N,max);
}