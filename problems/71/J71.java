class J71 {
	public static void main(String[] args) {
		int t = 3; 
		int b = 7;
		int d = 1000000;
		double diff = Double.POSITIVE_INFINITY;
		int up_j = 0;
		int up_i = 0;
		int x = 0;
		double s = 0.0; 
		for (int i = 1; i <= d; i++) {
			x = (3 * i) / 7;
			for (int j = 1; j <= x; j++) {
				s = ((double)t/b) - ((double)j/i);
				if (s < diff && s != 0) {
					diff = s;
					up_i = i;
					up_j = j;
				} 
			}
		}
		System.out.println(diff + " " + up_j + " " + up_i);
	}
}
