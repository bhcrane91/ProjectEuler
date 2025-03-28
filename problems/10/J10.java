import java.lang.Math;

class J10 {
	public static void main(String[] args) {
		int limit = 10;
		long ans = 0L;
		int numP = 0;
		for (int i = 0; i < limit; i++) {
			if (checkPrime(i)) {
				ans += (long)i;
				numP++;
				System.out.println(i + " ");
			}
		}
		System.out.println("Num Primes below " + limit + ": " + numP + " | Sum: " + ans);
	}

	public static boolean checkPrime(int n) {
		if (n <= 1)  return false;
		if (n == 2) return true;
		if (n % 2 == 0) return false;
		System.out.print(" " + ((int)Math.sqrt(n))+1);
		for (int i = 3; i < ((int)Math.sqrt(n))+1; i+=2) {
			System.out.println(n + " " + i);
			if (n % i == 0) return false;
		}
		return true;
	}
}
