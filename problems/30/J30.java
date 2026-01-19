class J30 {
	public static void main(String[] args) {
		int s = 2; 
		int ans = 0;
		int n = 5; 
		while (s < n+1) {
			for (int i = ((int) Math.pow(10,s)); i < ((int) Math.pow(10,s+1)); i++) {
				int j = i;
				int sj = 0;
				while (j > 0) {
					int l = j % 10;
					sj += ((int) Math.pow(l,5));
					j = (j - l) / 10;
				}
				if (sj == i) {
					ans += sj;
					// System.out.println(sj);
				}
			}
			s++;
		}
		System.out.println(ans);
	}
}
