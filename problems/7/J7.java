import java.lang.Math; 

class J7 {
	public static void main(String[] args) {
		int prime = 1;
		int n = 0;
		while (n < 10001) {
			prime++;
			if (checkPrime(prime)) n += 1;
		}
		System.out.println(n + "st prime = " + prime);
	}

	public static boolean checkPrime(int n) {
		if (n <= 1) return false;
		if (n == 2) return true;
		if (n % 2 == 0) return false;
		for (int i = 3; i < ((int)Math.sqrt(n))+1; i+=2) {
			if (n % i == 0) return false;
		}
		return true;
	}
}
