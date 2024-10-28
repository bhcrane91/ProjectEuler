class J686 {
	public static void main(String[] args) {
		System.out.println(p(123,678910));
	}

	public static long p(int L, long n) {
		double num = 2.0;
		long i = 0;
		int l = (int) Math.log10(L);
		long j = 0; 
		while (i < n) {
			if (((int)(num*Math.pow(10, l))) == L) i++;
			num *= 2;
			if (num > 10) num /= 10;
			j++;
		}
		return j;
	}
}
