class J76 {
	public static void main(String[] args) {
		System.out.println(dumb(100));
	}

	public static int dumb(int n) {
		int[] ways = new int[n+1];
		ways[0] = 1;
		for (int i = 1; i < n; i++) {
			for (int j = i; j <= 100; j++) {
				ways[j] += ways[j-i];
			}
		}
		return ways[n];
	}
}
