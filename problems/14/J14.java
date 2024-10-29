class J14 {
	public static void main(String[] args) {
		int target = 1000000;
		long[] c = collatz(113383);
		long max = 0;
		long num = 0;
		for (int i = 1; i < target; i++) {
			long[] seq = collatz(i);
			if (seq[1] > max) {
				max = seq[1];
				num = seq[0];
			}
		}
		System.out.println("Maximum Collatz Sequence for c[0] < " + target + ": c[0] = " + num + " | Length = " + max);
	}

	public static long[] collatz(int n) {
		long iters = 1L;
		long num = Long.valueOf(n);
		while (num != 1) {
			num = (num % 2 == 0) ? (num / 2) : (3*num + 1);
			iters++;
		}
		long[] ans = {n,iters};
		return ans;
	}
}
