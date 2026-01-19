import java.util.HashMap;
import java.util.ArrayList;
import java.lang.Math;
import java.lang.StringBuilder;

class J17 {
	public static void main(String[] args) {
		HashMap<Integer,String> numWords = new HashMap<>();

		numWords.put(0,"");
		numWords.put(10,"ten");
		numWords.put(20,"twenty");
		numWords.put(30,"thirty");
		numWords.put(40,"forty");
		numWords.put(50,"fifty");
		numWords.put(60,"sixty");
		numWords.put(70,"seventy");
		numWords.put(80,"eighty");
		numWords.put(90,"ninety");

		numWords.put(11,"eleven");
		numWords.put(12,"twelve");
		numWords.put(13,"thirteen");
		numWords.put(14,"fourteen");
		numWords.put(15,"fifteen");
		numWords.put(16,"sixteen");
		numWords.put(17,"seventeen");
		numWords.put(18,"eighteen");
		numWords.put(19,"nineteen");

    	numWords.put(100,"onehundred");
    	numWords.put(200,"twohundred");
    	numWords.put(300,"threehundred");
    	numWords.put(400,"fourhundred");
    	numWords.put(500,"fivehundred");
    	numWords.put(600,"sixhundred");
    	numWords.put(700,"sevenhundred");
    	numWords.put(800,"eighthundred");
    	numWords.put(900,"ninehundred");

    	numWords.put(0,"");
    	numWords.put(1,"one");
    	numWords.put(2,"two");
    	numWords.put(3,"three");
    	numWords.put(4,"four");
    	numWords.put(5,"five");
    	numWords.put(6,"six");
    	numWords.put(7,"seven");
    	numWords.put(8,"eight");
    	numWords.put(9,"nine");

		int letters = 0;
		StringBuilder numString = new StringBuilder();

		for (int i = 1; i < 1000; i++) {
			int teen = i % 100;
			int sub = 0;
			if (teen > 10 && teen < 20) {
				numString.append(numWords.get(teen));
				sub = teen;
			}
				
			ArrayList<Integer> num = parseNum(i-sub);
			for (int n: num) {
				if (n >= 100  && teen > 0) numString.append("and");
				numString.append(numWords.get(n));
			}
			
			letters += numString.length();

			// System.out.println(i + ": " + numString.toString() + " " + numString.length() + " " + letters);
			numString.setLength(0);
		}

		letters += "onethousand".length();
		System.out.println(letters);
	}

	public static ArrayList<Integer> parseNum(int n) {
		ArrayList<Integer> num = new ArrayList<>();
		int i = 1;
		while (n > 0) {
			int last = n % ((int) Math.pow(10,i));
			n -= last;
			i++;
			num.add(last);
		}
		return num;
	}
}
