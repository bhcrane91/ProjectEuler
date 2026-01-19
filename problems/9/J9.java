class J9 {
	public static void main(String[] args) {
		for (int a = 200; a < 1000; a++) {
			for (int b = a+1; b < 1000-a; b++) {
				int c = 1000 - a - b;
				if (a*a+b*b == c*c) {
					System.out.println("Triple: (" + a + "," + b + "," + c + ") | Product: " + a*b*c);
					return;
				}
			}
		}
	}
}
