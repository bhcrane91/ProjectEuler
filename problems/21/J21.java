import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.lang.Math;
import java.util.Set;

class J21 {
	public static void main(String[] args) {

		Set<Integer> amicable = new HashSet<>();
		for (int i = 1; i < 10000; i++) {
			if (!amicable.contains(i)) {
				int a = setSum(divisors(i));
				int b = setSum(divisors(a));
				if (b == i && a != b) {
					amicable.add(a);
					amicable.add(b);
				}
			}
		}
		System.out.println(setSum(amicable));
	}

	public static Set<Integer> divisors(int n) {
		Set<Integer> divs = new HashSet<>();
		divs.add(1);
		for (int i = 2; i < ((int) Math.sqrt(n))+1; i++) {
			if (n % i == 0) {
				divs.add(i);
				divs.add(n/i);
			}
		}
		return divs;
	}

	public static int setSum(Set<Integer> set) {
		int sum = 0; 
		for (int item: set) sum += item;
		return sum;
	}
}