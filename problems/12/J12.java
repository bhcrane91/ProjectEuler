import java.util.HashSet;
import java.util.Set;

class J12 {
	public static void main(String[] args) {
		long tri = 1L;
		long itr = 1L;
		Set<Long> divisors = divisors(tri);
		int target = 500;
		while (divisors.size()+2 <= target) {
			itr++;
			tri += itr;
			divisors = divisors(tri);
		}
		System.out.println("Triangle Number (" + itr + "): " + tri + " | Divisors: " + (divisors.size()+2));
	}

	public static Set<Long> divisors(long n) {
		Set<Long> divisors = new HashSet<>();
		for (long i = 2L; i < ((long)Math.sqrt(n))+1L; i++) {
			if (n % i == 0) {
				divisors.add(i);
				divisors.add(n/i);
			}
		}
		return divisors;
	}
}
