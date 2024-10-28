class J14 {
	public static void main(String[] args) {
		int max = 0; 
		int num = 0;
		int target = 1000000;
		collatz(113382);
		/*
		for (int i = 1; i < target; i++) {
			int[] seq = collatz(i);
			if (seq[1] > max) {
				max = seq[1];
				num = seq[0];
			}
			System.out.println(i);
		}
		*/
		System.out.println("Maximum Collatz Sequence for c[0] < " + target + ":");
		System.out.println("c[0] = " + num + " | Length = " + max);
	}

	public static int[] collatz(int n) {
		int iters = 1;
		int num = n;
		while (num != 1) {
			num = (num % 2 == 0) ? (num / 2) : (3*num + 1);
			iters++;
			System.out.println(num + " " + iters);
		}
		int[] ans = {n,iters};
		return ans;
	}
}
