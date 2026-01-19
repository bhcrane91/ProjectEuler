import java.lang.Math;
import java.util.ArrayList;
import java.util.List;

class J3 {
	public static void main(String[] args) {
		List<Long> list = new ArrayList<>();
		long n = 600851475143L;
		long num = n;
		while (n % 2 == 0) {
			list.add(2L);
			n /= 2;
		}
		for (long i = 3; i < ((long)Math.sqrt(n))+1; i+=2) {
			while (n % i == 0) {
				n /= i;
				list.add(i);
			}
		}
		if (n > 1) list.add(n);

		System.out.print("Prime Factors of " + num +  ": ");
		for (long j: list) {
			System.out.print(j + " ");
		}
		System.out.print("| Largest -> " + list.get(list.size()-1) + "\n");
	}

}
