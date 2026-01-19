import java.util.Set;
import java.util.stream.Collectors;
import java.util.HashSet;
import java.lang.Math;

class J45 {
	public static void main(String[] args) {
		Set<Integer> intersection = new HashSet<>();
		Set<Integer> pentagons = new HashSet<>();
		Set<Integer> hexagons = new HashSet<>();

		for (int i = 1; i < 100001; i += 2) {
			pentagons.add(pentagon(i));
			hexagons.add(hexagon(i));

			if (i-1 % 1000 == 0) {
				intersection = pentagons.stream().filter(hexagons::contains).collect(Collectors.toSet());
				if (intersection.size() >= 3) {
					break;
				}
			}
		}


		for (int shared: intersection) {
			System.out.println(shared);
		}
	}

	public static int hexagon(int n) {
		return n * (2 * n - 1);
	}

	public static int pentagon(int n) { 
		return n * (3 * n - 1) / 2;
	}
}
