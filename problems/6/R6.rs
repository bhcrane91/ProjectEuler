fn main() {
    let n = 100;
    let sum_of_squares = (n * (n+1) * (2*n + 1)) / 6;
    let mut square_of_sums = (n * (n+1)) / 2;
    square_of_sums *= square_of_sums;
    println!("{}", square_of_sums-sum_of_squares);
}