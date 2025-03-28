import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;
import java.util.ArrayList;

class J33 {
	public static void main(String[] args) {
		for (int j = 11; j < 100; j++) {
			for (int i = 10; i < j; i++) {
				List<Integer> a = digits(i);
				List<Integer> b = digits(j);

				List<Integer> result = a.stream()
					.distinct()
					.filter(b::contains)
  					.collect(Collectors.toList());

				if (i % 10 != 0 && j % 10 != 0 && !result.isEmpty()) {
					int r = result.get(0);
					a.remove(r);
					b.remove(r);

					if (b.get(0) != 0 && i/j == a.get(0)/b.get(0)) {
						System.out.println(i + " " + j + " " + a.get(0) + " " +  b.get(0));
					}
				}	
			}
		}
	}

	public static List<Integer> digits(int n) {
		List<Integer> digits = new ArrayList<>();
		while (n > 0) {
			int last = n % 10;
			digits.add(last);
			n = (n - last) / 10;
		}
		return digits;
	}
}
