import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.lang.StringBuilder;

class J8 {
	public static void main(String[] args) {
        String filePath = "num.txt";
        StringBuilder sb = new StringBuilder();
        
        try (Scanner scanner = new Scanner(new File(filePath))) {
            while (scanner.hasNextLine()) {
                sb.append(scanner.nextLine());
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        String num = sb.toString();
        // System.out.println(num);
        long max = 0L;
        String submax = "";
		int[] places = new int[2];
        for (int i = 0; i < num.length()-13; i++) {
            long curr = 1L;
            for (int j = 0; j < 13; j++) {
				curr *= (((int)num.charAt(i+j))-48);
            }
			if (curr > max) {
				max = curr;
				submax = num.substring(i, i+13);
			}
        }
		System.out.println(max + " | " + submax);
	}
}
