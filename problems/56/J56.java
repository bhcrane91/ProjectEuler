import java.lang.Math;
import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;

class J56 {
	public static void main(String[] args) {
		int N = 100;
		int m = 0; 
		for (int a = 1; a < N; a++) {
			for (int b = 1; b < N; b++) {
				int c = listSum(exponential(a, b));
				m = (c > m) ? c : m;
			}
		}
		System.out.println("Maximal Digit Sum of a**b for a, b < " + N + ": " + m);
	}

	public static List<Integer> digits(int n) {
		List<Integer> number = new ArrayList<>();
		while (n > 0) {
			int l = n % 10;
			number.add(l);
			n = (n - l) / 10;
		}
		return number;
	}

	public static int listSum(List<Integer> list) {
		int S = 0;
		for (Integer s: list) S += s;
		return S;
	}

	public static List<Integer> exponential(int a, int b)
	{
		List<Integer> numA = digits(a);
		for (int i = 0; i < b; i++) {
			int remainder = 0;
			for (int j = 0; j < numA.size(); j++) {
				remainder = numA.get(j) * a + remainder;
				numA.set(j, (remainder % 10));
				remainder /= 10;
			}
			while (remainder > 0) {
				int l = remainder % 10;
				numA.add(l);
				remainder = (remainder - l) / 10;
			}
			// System.out.println(numA.toString() + " " + numA.size() + " " + remainder);
		}
		return numA;
	}

	/*
	public static int[] digits(int n) {
		int k = String.valueOf(n).length();
		int[] d = new int[k];
		for (int i = k; i > 0; i--) {
			int l = n % 10; 
			d[i-1] = l;
			n = (n - l) / 10;
		}
		return d;
	}

	public static int arrSum(int[] arr) {
		int S = 0;
		for (int n: arr) S += n;
		return S;
	}

	public int[] multiply(int[] arr, int n) {
		int prod = 0;
		for (int i = 0; i < arr.length; i++) {
			prod += arr[i] * n;
			arr[i] = prod % 10;
			prod /= 10;
		}

		if (prod > 0) {
			int[] remainder = digits(n);

		}
	}

	public static int[] exponential(int a, int b) {
		int
	}*/
}
