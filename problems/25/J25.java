class J25 {
	public static void main(String[] args) {
		double a = 1.0;
		double b = 1.0;
		int i = 0;
		int x = 0;
		while (x < 1000) {
			double n = a + b;
			a = b; 
			b = n;
			i++;
			if (String.valueOf(b).contains("E")) {
				a /= 10;
				b /= 10;
				x += 1;
			}
		}
		System.out.println(i + " " + a + " " + b);
	}
}
