import java.util.Arrays;

class J15 {
	public static void main(String[] args) {
		int target = 20;
		long[] triangle = pascal(target);
		long max = Arrays.stream(triangle).max().orElseThrow();
		System.out.println("Paths in " + target + "x" + target + " square: " + max);
	}

	public static long[] pascal(int n) {
		long[] pascalRow = new long[2*n];
		pascalRow[0] = 1L;
		for (int row = 0; row < 2*n; row++) {
			for (int i = 0; i < 2*n; i++) {
				pascalRow[i] += pascalRow[(i+1)%(2*n)];
			}
		}
		return pascalRow;
	}
}
