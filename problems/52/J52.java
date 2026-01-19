import java.lang.Math;
import java.util.Arrays;
import java.util.List;

class J52 {
	public static void main(String[] args) {
		for (int i = 1; i < 5; i++) { 
			int j = pow(10,i) + 6 + Integer.valueOf(i > 0 ? "1".repeat(i) : "1") + 1;
			for (int k = i; i < j; k++) {
				String one = String.join("",strSort(String.valueOf(k)));
				int score = 1;
				for (int l = 2; l <= 6; l++) {
					String nStr = String.join("",strSort(String.valueOf(k*l)));
					if (nStr.equals(one)) score++;
				}
				if (score == 6) {
					System.out.println(k + Arrays.asList(k,k*2,k*3,k*4,k*5,k*6).toString());
					System.exit(0);
				}
			}
		}	
	}

	public static int pow(int a, int b) {
		return (int) Math.pow(a,b);
	}

	public static String strSort(String s) {
		char[] word = s.toCharArray();
		Arrays.sort(word);
		return new String(word);
	}
}
