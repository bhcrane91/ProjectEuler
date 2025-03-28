import java.util.ArrayList;
import java.util.List;
import java.lang.Math;

class J5 {
	public static void main(String[] args) {
		long myLCM = 1L;
		long top = 20L;
		for (long i = 2L; i <= top; i++) {
			myLCM = lcm(myLCM,i);
		}
		System.out.println("J -> " + myLCM);
	}

	public static List<Long> prime_factors(long n) {
		if (n <= 1) return new ArrayList<>();
		List<Long> factors = new ArrayList<>();
		while (n % 2 == 0) {
			factors.add(2L);
			n /= 2;
		}
		for (long i = 3L; i < ((long)Math.sqrt(n))+1L; i+=2L) {
			while (n % i == 0) {
				factors.add(i);
				n /= i;
			}
		}
		if (n > 1L) factors.add(n);
		return factors;
	}

	public static long gcd(long a, long b) {
		List<Long> primeFactorsA = prime_factors(a);
		List<Long> primeFactorsB = prime_factors(b);
		long div = 1L;
		for (long n: primeFactorsA) {
			if (primeFactorsB.contains(n)) {
				div *= n;
				primeFactorsB.remove(primeFactorsB.indexOf(n));
			}
		}
		return div;
	}

	public static long lcm(long a, long b) {
		return a*b/gcd(a,b);
	}
}
