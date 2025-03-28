import java.lang.Math;
import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;

class J39 {
	public static void main(String[] args) {
		int target = 1000;
		int[] max = {0,0}; 
		HashMap<Integer,Integer> triangles = new HashMap<>();
		for (int m = 2; m <= 100; m++) {
			for (int n = 1; n <= m; n++) {
				for (int k = 1; k <= 100; k++) {
					if (coprime(m, n) && (m + n) % 2 != 0) {
						int triple = triple(k,m,n);
						if (triple < target) {
							if (triangles.containsKey(triple)) {
								triangles.put(triple, triangles.get(triple) + 1);
								if (triangles.get(triple) > max[0]) {
									max[0] = triangles.get(triple);
									max[1] = triple;
								}
							}
							else {
								triangles.put(triple, 1);
							}
						}
 					}
				}
			}
		}
		System.out.println(max[0] + " " + max[1]);
	}

	public static int triple(int k, int m, int n) {
		int a = k * (m*m - n*n);
		int b = k * (2*m*n);
		int c = k * (m*m + n*n);
		return a + b + c;
	}

	public static boolean coprime(int a, int b) {
		return gcd(a,b) == 1;
	}

	public static List<Integer> prime_factors(int n) {
		if (n <= 1) return new ArrayList<>();
		List<Integer> factors = new ArrayList<>();
		while (n % 2 == 0) {
			factors.add(2);
			n /= 2;
		}
		for (int i = 3; i < ((int)Math.sqrt(n))+1L; i+=2L) {
			while (n % i == 0) {
				factors.add(i);
				n /= i;
			}
		}
		if (n > 1L) factors.add(n);
		return factors;
	}

	public static int gcd(int a, int b) {
		List<Integer> primeFactorsA = prime_factors(a);
		List<Integer> primeFactorsB = prime_factors(b);
		int div = 1;
		for (int n: primeFactorsA) {
			if (primeFactorsB.contains(n)) {
				div *= n;
				primeFactorsB.remove(primeFactorsB.indexOf(n));
			}
		}
		return div;
	}
}
