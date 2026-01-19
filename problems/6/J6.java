class J6 {
	public static void main(String[] args) {
		long n = 100L;
		long sumOfSquares = (n * (n+1) * (2*n + 1)) / 6;
		long squareOfSums = (n * (n+1)) / 2;
		squareOfSums *= squareOfSums;
		System.out.println((squareOfSums - sumOfSquares));
	}
}
