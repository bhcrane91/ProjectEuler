import java.lang.Math;
import java.lang.StringBuilder;

class J4 {
	public static void main(String[] args) {
		int digits = 3; 
		int bot = (int) Math.pow(10, digits-1);
		int top = (int) Math.pow(10, digits);
		int[] max = new int[3];
		for (int i = top; i >= bot; i--) {
			for (int j = i; j >= bot; j--) {
				int p = i*j;
				String str = String.valueOf(p);
				if (p > max[0] && checkPalindrome(str)) {
					max[0] = p;
					max[1] = i;
					max[2] = j;
				}
			}
		}
		System.out.println("Java | Max: " +  max[0] + " | Factors: (" + max[1] + "," + max[2] + ")");
	}

	public static boolean checkPalindrome(String str) {
		for(int i = 0; i < str.length(); i++) {
			if (str.charAt(i) != str.charAt(str.length()-i-1)) {
				return false;
			}
		}
		return true;
	}
}
