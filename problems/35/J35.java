import java.lang.Math;

class J35 {
	public static void main(String[] args) {
		int N = 7;
		int S = 0;
		int n = 10;
		for (int i = 1; i < N; i++) {
			for (int j = n/10; j < n; j++) {
				int tmp = j;
				int ts = 0;
				// StringBuilder sb = new StringBuilder();
				for (int k = 0; k < i; k++) {
					boolean b = checkPrime(tmp);
					// sb.append("(" + i + "," + j + ") -->" + tmp + " (" + b + ")\n");
					if (b) ts++;
					tmp = ((n/10) * (tmp % 10)) + ((tmp - (tmp % 10)) / 10);
				}
				
				if (ts == i) {
					// System.out.print(sb.toString());
					// System.out.println("Adding " + j);
					S++;
				}
			}
			n *= 10;
		}
		System.out.println("Number of Circular Primes below " + (n/10) + ": " + S);

		/**int N = 1847295;
		int m = (int)Math.log10(N);
		int n = (int)Math.pow(10,m);
		int tmp = N;
		for (int i = 0; i < m; i++)
		{
			int a = (n);
			int b = (tmp % 10);
			int c = (tmp - b) / 10;
			System.out.print("a: " + a + "\n" + "b:     " + b + "\nc:" + c + "\n");
			tmp = (a * b) + c;
			System.out.println(tmp + " ");
		}**/
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
