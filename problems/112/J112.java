import java.lang.StringBuilder;
import java.util.Arrays;

class J112 {
	public static void main(String[] args) {
		int bouncy = 0;
		int total = 99;
		StringBuilder sb = new StringBuilder();
		while (bouncy*100 < total*99) { // need this version instead of float comparison 
			// do to 
			total++;
			String num = String.valueOf(total);
			char[] sorted = num.toCharArray();
			Arrays.sort(sorted);
			String up = new String(sorted);
			String down = sb.append(up).reverse().toString();
			if (!num.equals(down) && !num.equals(up)) {
				bouncy++;
			}
			sb.setLength(0);
		}
		System.out.println(((double)bouncy/total) + " " + total + " " + bouncy);
	}

}
