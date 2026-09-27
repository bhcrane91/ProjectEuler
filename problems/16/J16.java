import java.lang.Math;
import java.util.List;
import java.util.ArrayList;

class J16 {
	public static void main(String[] args) {
		int b = 2;
    	int e = 1000;
    	List<Integer> res = exp(b,e);
    	int S = 0;
    	for (int n = 0; n < res.size(); n++) S += res.get(n);
    	System.out.println("Sum of digits of " + b  + "^" + e + ": " + S);
	}

	public static List<Integer> exp(int base, int exp) {
		List<Integer> num = new ArrayList<>(); 
		num.add(base);
		for (int i = 1; i < exp; i++) {
			int rem = 0; 
			for (int j = 0; j < num.size(); j++) {
				int curr = (num.get(j) * base) + rem;
				if (curr < 10) {
					num.set(j, curr);
					rem = 0;
				} else {
					num.set(j,curr % 10);
					rem = curr / 10;
				}
			}
			if (rem > 0) num.add(rem);
		}
		return num;
	}
}
