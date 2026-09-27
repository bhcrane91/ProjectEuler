import helper.Algos;

class J7 {
	public static void main(String[] args) {
		int prime = 1;
		int n = 0;
		while (n < 10001) {
			prime++;
			if (Algos.checkPrime(prime)) n += 1;
		}
		System.out.println(n + "st prime = " + prime);
	}
}
