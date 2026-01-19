class J1 {
	public static void main(String[] args) {
		int ans = 0;
		// int arg = Integer.valueOf(args[0]);
		int arg = 1000;
		for (int i = 0; i < arg; i++) ans += i % 5 == 0 || i % 3 == 0 ? i : 0;
		System.out.println("Sum of multiples of 3 or 5 below " + arg + ": " + ans);
	}
}
