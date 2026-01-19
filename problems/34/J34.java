import java.util.*;

class J34 {
	public static void main(String[] args) {

		HashMap<Integer,Integer> factorials = new HashMap<>();
		for (int i = 0; i < 10; i++) { 
			factorials.put(i,factorial(i));
		}

		List<Integer> digitFactorials = new ArrayList<>();
		int ans = 0; 
		for (int i = 3; i < 1000000; i++) {
			int num = i;
			int sum = 0;
			while (num > 0) { 
				int last = num % 10; 
				num = (num - last) / 10;
				sum += factorials.get(last);
				if (sum > i) num = 0;
			}

			if (sum == i) {
				ans += i; 
			}
		}

		System.out.println(ans);
	}

	public static int factorial(int n) { 
		if (n < 1) return 1;
		int f = 1;
		for (int i = 1; i <= n; i++) f *= i;
		return f;
	}
}
