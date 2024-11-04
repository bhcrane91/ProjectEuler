import java.lang.Math;
import java.util.ArrayList;
import java.util.List;

class J27 {
	public static void main(String[] args) {
		List<Integer> pb = primesBelow(1000);
		// List<Integer> ps = firstNPrimes(200);
		int[] streak = new int[3];
		for (int a = -999; a < 1000; a++) {
			for (int b: pb) {
				int curr = quadratic(a,b,1);
				int run = 1;
				while (pb.contains(curr)) {
					run++;
					curr = quadratic(a,b,run);
				}
				if (run > streak[0]) {
					int[] tmp = {run,a,b};
					streak = tmp;
				}
			}
		}
		System.out.println("Streak: " + streak[0] + " | a = " + streak[1] + ", b = " + streak[2] + " | a*b = " + (streak[1]*streak[2]));
	}

	public static int quadratic(int a, int b, int n) {
		return (n*n) + (a*n) + b;
	}

	public static boolean checkPrime(int n) {
		if (n <= 1) return false;
		if (n == 2) return true;
		if (n % 2 == 0)  return false;
		for (int i = 3; i < ((int)Math.sqrt(n))+1; i+=2) {
			if (n % i == 0) return false;
		}
		return true;
	}

	public static List<Integer> firstNPrimes(int n) {
		List<Integer> l = new ArrayList<>();
		int i = 1;
		while (l.size() < n) {
			if (checkPrime(i)) l.add(i);
			i++;
		}
		return l;
	}

	public static List<Integer> primesBelow(int n) {
		List<Integer> l = new ArrayList<>();
		for (int i = 2; i < n; i++) {
			if (checkPrime(i)) l.add(i);
		}
		return l;
	}
}
