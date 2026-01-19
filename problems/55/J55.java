class J55 {
	public static void main(String[] args) {
		long lychrel = 0;
		long N = 10000;
		for (long i = 1; i < N; i++) {
			long n = i;
			boolean l = true;
			long j = 0;
			while (j < 50 && l == true) {
				System.out.println(i + " " + n);
				long r = reverse(n);
				n += r;
				l = (n == r) ? false : true;
				j++;
			}
			lychrel += l == true ? 1 : 0;
		}
		System.out.println(lychrel);
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
