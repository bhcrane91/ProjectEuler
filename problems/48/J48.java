class J48 {
	public static void main(String[] args) {
		long sum = 0;
		long d = (long) Math.pow(10,10);
		for (int i = 1; i < 1001; i++) {
			sum += modExp(i, i, d);
		}
		System.out.println(sum % d);
	}
	
	public static long modExp(int a, int b, long d) {
		if (b == 0) return 1;
		long s = 1;
		for (int i = 0; i < b; i++) {
			s = (s * a) % d;
		}
		return s;
	}
}
