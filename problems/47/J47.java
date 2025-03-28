import java.util.ArrayList;
import java.util.List;
import java.util.Set;
import java.util.HashSet;
import java.lang.Math;

class J47 {
	public static void main(String[] args) {
		int streak = 0;
		int distinct = 4;
		int n = 210;
		List<Integer> numStreak = new ArrayList<>();

		while (streak != distinct) {
			Set<Integer> pfs = primeFactors(n);
			if (pfs.size() == distinct) {
				streak += 1;
				numStreak.add(n);
			} else if (streak > 0 && pfs.size() != distinct) {
				streak = 0;
				numStreak.clear();
			}
			n++;
		}

		System.out.println(numStreak.toString());
	}

	public static Set<Integer> primeFactors(int n) {
		Set<Integer> pf = new HashSet<>();

		if (n == 2) {
			pf.add(2);
			return pf;
		}

		while (n % 2 == 0) {
			pf.add(2);
			n /= 2;
		}

		for (int i = 3; i < Math.sqrt(n)+1; i += 2) {
			while (n % i == 0) {
				pf.add(i);
				n /= i;
			}
		}

		if (n > 1) pf.add(n);

		return pf;
	}


}
