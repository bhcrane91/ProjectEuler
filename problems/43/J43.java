import java.util.*;

class J43 {
    
    static int[] primes = {2, 3, 5, 7, 11, 13, 17};
    static long sum = 0;

    public static void main(String[] args) {
        List<String> digits = new ArrayList<>();
        for (int i = 0; i <= 9; i++) {
            digits.add(String.valueOf(i));
        }

        permute(digits, 0);
        System.out.println(sum);
    }

    // Generates permutations of the digits list
    static void permute(List<String> arr, int index) {
        if (index == arr.size() - 1) {
            checkAndAdd(arr);
            return;
        }

        for (int i = index; i < arr.size(); i++) {
            Collections.swap(arr, index, i);
            permute(arr, index + 1);
            Collections.swap(arr, index, i); // backtrack
        }
    }

    // Checks the substring divisibility property
    static void checkAndAdd(List<String> perm) {
        for (int i = 1; i <= 7; i++) {
            int num = Integer.parseInt(perm.get(i) + perm.get(i + 1) + perm.get(i + 2));
            if (num % primes[i - 1] != 0) {
                return;
            }
        }

        StringBuilder number = new StringBuilder();
        for (String d : perm) {
            number.append(d);
        }
        long val = Long.parseLong(number.toString());
        sum += val;
        // System.out.println(val + " " + sum);
    }
}