import java.util.ArrayList;
import java.util.List;
import java.lang.Math;

class J5 {
	public static void main(String[] args) {
		int ans = 1;
		for (int i = 1; i < 20; i++) {
			ans = lcm(i,ans);
		}
		System.out.println(ans);
	}

	public static int gcd(int a, int b) {
		int temp = b;
		while (b != 0) {
			temp = b;
			b = a % b;
			a = temp;
		}
		return a;
	}

	public static int lcm(int a, int b) {
		return (a * b) / gcd(a, b);
	}


}
