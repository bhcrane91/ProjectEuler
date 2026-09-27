class J71 {
	public static void main(String[] args) {
		int t = 3; 
		int b = 7;
		int l = 1000000;
		double D = Double.POSITIVE_INFINITY;
		int n = 0;
		int d = 0;
		for (int i = l - 1; i > 0; i--) {
			int q = (t * i) / b;
			double s = ((double)t/b) - ((double)q/i);
			if (s < D && s != 0) {
				D = s;
				n = q;
				d = i;
			}
		}
		System.out.println(n + " " + d);
	}
}
