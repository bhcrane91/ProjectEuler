import java.lang.Math;

class J40 {
	public static void main(String[] args) {
		int i = 1000000, j = 0, n = 1, pow = 0, ans = 1;
		while (j < i) {
			ans *= (n % 10);
			for (int p = ((int) Math.pow(10,pow)); p < (int) Math.pow(10,pow+1); p++) {
				n += 1;
				j += (p+1);
			}
			pow += 1;
			System.out.println(n + " " + ans + " " + j + " " + pow);
		}

	}
}
