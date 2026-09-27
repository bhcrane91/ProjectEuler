class J55 {
	public static void main(String[] args) {
		int lychrel = 0;
		long N = 10000;
		for (long i = 1; i < N; i++) {
			long n = i;
		 	int l = 1;
			for (int j = 0; j < 50; j++) {
				n += reverse(n);
				if (n == reverse(n)) {
					l = 0;
					break;
				}
			}
			lychrel += l;
		}
		System.out.println("Lychrel Numbers below " + N + ": " + lychrel);
	}

	public static long reverse(long n) {
		long r = 0;
		while (n > 0) {
			r = r * 10 + n % 10;
			n /= 10;
		}
		return r;
	}
}
