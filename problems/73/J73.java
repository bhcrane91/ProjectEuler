import java.util.HashSet;
import java.util.Set;

class J73 {
	public static void main(String[] args) {
		int T = 12000;
		int S = 0;
		Set<String> fractions = new HashSet<>();
		fractions.add("1/3");
		fractions.add("1/2");

		for (int d = 4; d <= T; d++) {

			int b = d / 3 + 1;
			int t = d / 2;

			for (int f = b; f <= t; f++) {

				int frac_n = f;
				int frac_d = d;
				int g = gcd(frac_n,frac_d);

				while (g != 1) {

					frac_n /= g;
					frac_d /= g;
					g = gcd(frac_n, frac_d);
				}

				String fraction = frac_n + "/" + frac_d;
				if (!fractions.contains(fraction)) {
					S++;
					fractions.add(fraction);
				}
			}
	
		}

		System.out.println(S);
	}

	public static int gcd(int a, int b) {
		int tmp = b;
		while (b != 0) {
			tmp = b;
			b = a % b;
			a = tmp;
		}
		return a;
	}
}
