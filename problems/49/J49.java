import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;
import java.lang.Math;

class J49 {
	public static void main(String[] args) {
		
		int pow = 4;
		Set<Integer> primes = new HashSet<>();
		for (int i = (int) Math.pow(10,pow-1); i < (int) Math.pow(10,pow); i++) {
			if (checkPrime(i)) primes.add(i);
		}
		
		int target = 3330;
		List<List<Integer>> triplets = new ArrayList<>();
		for (int a: primes) {
			for (int b: primes) {
				if (a < b) {
					int d = b - a;
					if (primes.contains(b + d) && d == target) {
						List<Integer> triple = Arrays.asList(a,b,b+d);
						boolean trip = true;
						String nStr = String.join("",strSort(String.valueOf(triple.get(0))));
						for (int j = 1; j < triple.size(); j++) {
							if (!String.join("",strSort(String.valueOf(triple.get(j)))).equals(nStr)) trip = false;
						}
						if (trip) triplets.add(triple);
					}
				}
			}
		}
		for (List<Integer> l: triplets) {
			System.out.println(l.toString() + " " + l.stream().map(String::valueOf).collect(Collectors.joining()));
		}
	}

	public static boolean checkPrime(int n) {
		if (n < 2) return false;
		if (n == 2) return true;
		if (n % 2 == 0) return false;
		for (int i = 3; i < Math.sqrt(n)+1; i+=2) {
			if (n % i == 0) return false;
		}
		return true;
	}

	public static String strSort(String s) {
		char[] word = s.toCharArray();
		Arrays.sort(word);
		return new String(word);
	}
}
