import java.util.Set;
import java.util.HashSet;

class J44 {
	public static void main(String[] args) {
		int N = 5000;
		int[] pentagons = new int[N];
		for (int i = 1; i <= N; i++) {
			pentagons[N-i] = pentagon(i);
		}
		int[] D = new int[3];
		D[0] = Integer.MAX_VALUE;
		for (int s = 0; s < N; j++) {
			for (int d = s+1; d < N; d++) {
				
				if (pentagons.contains(s) && pentagons.contains(d) && d < D[0]) {
					D[0] = d;
					D[1] = j;
					D[2] = k;
					System.out.println(d + " " + j + " " + k);
					break;
				}
			}
		}
	}

	public static int pentagon(int n) {
		return ((3 * n * n) - n) / 2;
	}

	public static int checkPentagon(int n) {

	}
}
