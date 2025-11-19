class J37 {
	public static void main(String[] args) {
		int truncatable = 11;
		int prime = nextPrime(10);
		int sum = 0;
		while (truncatable > 0) {
			String strPrime = String.valueOf(prime);
			boolean trunc = true;
			for (int i = 1; i < strPrime.length(); i++) {
				if (!checkPrime(Integer.valueOf(strPrime.substring(i))) || !checkPrime(Integer.valueOf(strPrime.substring(0, i)))) {
					trunc = false;
				}
			}
			if (trunc) {
				System.out.println(prime);
				truncatable -= 1;
				sum += prime;
			}
			prime = nextPrime(prime);
		}
		System.out.println(sum);
	}

	public static boolean checkPrime(int n) {
		if (n <= 1) return false;
		if (n == 2) return true;
		if (n % 2 == 0)  return false;
		for (int i = 3; i < Math.sqrt(n)+1; i += 2) {
			if (n % i == 0) return false;
		}
		return true;
	}

	public static int nextPrime(int n) {
		n++;
		while (!checkPrime(n)) n++;
		return n;
	}

}
