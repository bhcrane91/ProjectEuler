import java.util.Arrays; 

class J20 {
	public static void main(String[] args) {
		int n = 100;
		int[] fact = factorial(n);
		int s = 0;
		for (int i: fact) s += i;
		System.out.println("Sum of digits of " + n + "! = " + s);

	}

	public static int[] factorial(int num) {
		int[] arr = {1};
		for (int i = 2; i <= num; i++) {
			arr = multiply(arr, i);
		}
		
		for (int j = arr.length - 1; j >= 0; j--) {
			if (arr[j] != 0) {
				arr = Arrays.copyOfRange(arr, 0, j+1);
				break;
			}
		}
		return arr;
		/* 
		StringBuilder sb = new StringBuilder();
		for (int i: arr) {
			sb.append(String.valueOf(i));
		}
		return sb.reverse().toString();
		*/
	}

	public static int[] multiply(int[] num, int f) {
		int rollover = 0;
		int curr = 0;

		int[] newarr = new int[num.length + String.valueOf(f).length()];
		for (int i = 0; i < num.length; i++) {
			curr = num[i] * f + rollover;
			newarr[i] = curr % 10;
			rollover = curr / 10;
		}
		return newarr;
	}
}
