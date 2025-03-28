import java.util.Set;
import java.util.HashSet;

class J44 {
	public static void main(String[] args) {
		Set<Integer> pentagons = new HashSet<>();
		for (int i = 1; i <= 5000; i++) {
			pentagons.add(pentagon(i));
		}
		int[] D = new int[3];
		D[0] = Integer.MAX_VALUE;
		for (int j: pentagons) {
			for (int k: pentagons) {
				int s = j + k;
				int d = j - k;
				if (pentagons.contains(s) && pentagons.contains(d) && d < D[0]) {
					D[0] = d;
					D[1] = j;
					D[2] = k;
					System.out.println(d + " " + j + " " + k);
				}
			}
		}
	}

	public static int pentagon(int n) {
		return ((3 * n * n) - n) / 2;
	}
}
