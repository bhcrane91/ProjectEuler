class J58 {
	public static void main(String[] args) {
		int s = 4; 
		int n = 9;
		int corners = 5;
		int primes = 3;
		while (((double)primes/corners) > 0.1) {
			for (int i = 0; i < 4; i++) {
				n += s;
				if (checkPrime(n)) primes++;
				corners++;
			}
			s += 2;
		}
		System.out.println(s + " " + primes + " " + corners + " " + ((float)primes/corners));
	}

	public static boolean checkPrime(int n) {
		if (n <= 1) return false;
		if (n == 2) return true;
		if (n % 2 == 0)  return false;
		for (int i = 3; i < ((int)Math.sqrt(n))+1; i+=2) {
			if (n % i == 0) return false;
		}
		return true;
	}
}
