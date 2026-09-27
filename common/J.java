class J {

    public J() {

    }

    public static Set<Integer> primeFactors(int n) {
		Set<Integer> pf = new HashSet<>();
		if (n == 2) {
			pf.add(2);
			return pf;
		}
		while (n % 2 == 0) {
			pf.add(2);
			n /= 2;
		}
		for (int i = 3; i < Math.sqrt(n)+1; i += 2) {
			while (n % i == 0) {
				pf.add(i);
				n /= i;
			}
		}
		if (n > 1) pf.add(n);
		return pf;
	}
}
