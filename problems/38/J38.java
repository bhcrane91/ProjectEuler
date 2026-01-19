import java.util.Arrays;
import java.math.*;

class J38 {
    public static void main(String[] arg) {
        int max = 0; 
        int nmx = 0;
        int[] comparator = {1,1,1,1,1,1,1,1,1};
        for (int n = 1; n < 6; n++) {
            int lb = (int) (9.0*Math.pow(10,n-1) + (Math.pow(10,n-1)-1)/9);
            int ub = (int) Math.pow(10,n);
            for (int i = lb; i < ub; i += 2) {
                int[] curr = new int[9];
                int j = 0; 
                String s = "";
                while (!Arrays.equals(curr, comparator) && j < 9) {
                    j++;
                    int k = i*j;
                    s = s.concat(String.valueOf(k)); 
                    if (!s.contains("0")) {
                        while (k > 0) {
                            int l = k % 10;
                            curr[l-1] += 1;
                            k = (k - l) / 10;
                        }
                    } else {
                        j = 10;
                    }
                }
                if (Arrays.equals(curr, comparator)) {
                    int newmax = Integer.valueOf(s);
                    if (newmax > nmx) {
                        max = i;
                        nmx = newmax;
                    }
                }
            }
        }
        System.out.print(max + " " + nmx);
    }
}