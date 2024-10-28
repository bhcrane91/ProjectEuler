import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.io.File;

class J13 {
	public static void main(String[] args) {
		List<List<String>> convert = new ArrayList<>();
		try {
			Scanner sc = new Scanner(new File("digits.txt"));
			while (sc.hasNextLine()) {
				List<String> line = new ArrayList<>(Arrays.asList(sc.nextLine().split("")));
				convert.add(line);
			}
			sc.close();
		} catch (Exception e) {
			System.out.print(e);
			System.exit(0);
		}
		long[][] arr = transpose(convert);
		long ans = 0L;
		long r = 0L; 
		
		for (int row = arr.length-1; row >= 0; row--) {
			long rowsum = 0;
			for (int col = 0; col < arr[row].length; col++) {
				rowsum += arr[row][col];
			}
			Long rSum = (Long) rowsum;
			ans += (r + (rSum % 10L));
			r = rSum / 10;
			if (String.valueOf(ans).length() > 10) {
				ans /= 10;
			}
		}
		System.out.println(ans);
		
	}

	public static long[][] transpose(List<List<String>> arr) {
		int i = arr.get(0).size();
		int j = arr.size();
		long[][] neu = new long[i][j];
		for (int k = 0; k < i; k++) {
			for (int n = 0; n < j; n++) {
				neu[k][n] = Long.valueOf(arr.get(n).get(k));
			}
		}
		return neu;
	}
}
