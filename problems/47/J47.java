import java.util.ArrayList;
import java.util.List;
import java.util.Set;
import java.util.HashSet;
import java.lang.Math;

class J47 {
	public static void main(String[] args) {
		int streak = 0;
		int distinct = 4;
		int n = 646;
		while (streak != distinct) {
			n++;
			int pfs = numDistinctPrimeFactors(n);
			streak = (pfs == distinct) ? streak + 1 : 0;
		}
		System.out.println("Streak: " + (n-distinct+1) + " -> " + n);
	}

	public static int numDistinctPrimeFactors(int n) {
		int f = 0;
		if (n % 2 == 0) {
			f++;
			while (n % 2 == 0) n /= 2;
		}
		for (int i = 3; i < Math.sqrt(n)+1; i += 2) {
			if (n % i == 0) {
				f++;
				while (n % i == 0) n /= i;
			}
		}
		if (n > 1) f++;
		return f;
	}


}
