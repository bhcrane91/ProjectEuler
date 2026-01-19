import java.util.HashSet;
import java.util.Set;
import java.lang.Math;

class J29 {
	public static void main(String[] args) {
		Set<Double> set = new HashSet<>();
		int n = 100;
		for (int i = 2; i <= n; i++) {
			for (int j = 2; j <= n; j++) {
				set.add(Math.pow(i,j));
			}
		}
		System.out.println(set.size());
	}
}
