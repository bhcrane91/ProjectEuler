import java.io.File;
import java.util.Scanner;

class J99 {
	public static void main(String[] args) {
		double maxVal = 0L;
		int maxidx = 0;
		int i = 0; 
		try {
			Scanner sc = new Scanner(new File("base_exp.txt"));
			while (sc.hasNextLine()) {
				String[] pair = sc.nextLine().split(",");
				double n = Double.valueOf(pair[1]) * Math.log(Double.valueOf(pair[0]));
				if (n > maxVal) {
					maxVal = n;
					maxidx = i;
				}
				i++;
			}
			// System.out.println(maxVal + " " + maxPair[0] + " " + maxPair[1] + " " + (maxidx+1));
			sc.close();
		}
		catch (Exception e) {
			e.printStackTrace();
			return;
		}
		System.out.println("J: Answer -> Max Value: " + maxVal + " | Line Number: " + (maxidx+1));
	}
}
