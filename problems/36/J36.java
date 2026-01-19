class J36 {
	public static void main(String[] args) {
		int sum = 0;
		for (int i = 1; i < 1000000; i++) { 
			if (palindrome(String.valueOf(i)) && palindrome(toBinary(i))) sum += i; 
		}
		System.out.println(sum);
	}	

	public static String toBinary(int n) {
		StringBuilder sb = new StringBuilder();
		int i = 1; 
		while (i <= n) {
			if ((i & n) > 0) sb.append("1");
			else sb.append("0");
			i *= 2;
		}
		return sb.reverse().toString();
	}

	public static boolean palindrome(String s) {
		return s.equals(new StringBuilder(s).reverse().toString());
	}
}
