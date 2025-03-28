import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.HashSet;
import java.util.Set;

class J32 {

    private static final Set<Integer> digits = new HashSet<>(Arrays.asList(1,2,3,4,5,6,7,8,9));
    private static final Set<Integer> other = new HashSet<>(Arrays.asList(1,2,3,4,5,6,7,8));


    public static void main(String[] args) {
        List<List<Integer>> partitions = partitionWithKParts(9, 3, other, null);
        Set<Integer> possibilities = new HashSet<>();
        int ans = 0; 
        for (List<Integer> partition: partitions) {
            for (int i = ((int) Math.pow(10,partition.get(1)-1)); i < ((int) Math.pow(10,partition.get(1))); i++) {
                for (int j = ((int) Math.pow(10,partition.get(2)-1)); j < ((int) Math.pow(10,partition.get(2))); j++) {
                    int k = i * j;
                    String s = k + "" + j + "" + i;
                    char[] currDigits = s.toCharArray();
                    Arrays.sort(currDigits);

                    if (!possibilities.contains(k) && s.length() == 9 && "123456789".equals(new String(currDigits))) {
                        System.out.println(i + " " + j + " " + k + " " + s);
                        possibilities.add(k);
                        ans += k;
                    }
                }
            }
        }
        System.out.println(ans);
	}

    public static List<List<Integer>> partitionWithKParts(int n, int k, Set<Integer> allowed, Integer maxValue) {
        if (maxValue == null) {
            maxValue = n; // By default, the maximum value of any part is n
        }

        if (k == 0) {
            if (n == 0) {
                List<List<Integer>> baseCase = new ArrayList<>();
                baseCase.add(new ArrayList<>());
                return baseCase;
            } else {
                return new ArrayList<>();
            }
        }

        if (n == 0) {
            return new ArrayList<>();
        }

        List<List<Integer>> partitions = new ArrayList<>();

        // Iterate from the minimum possible value for a partition part to maxValue
        for (int i = Math.min(n, maxValue); i > 0; i--) {
            if (allowed.contains(i)) {
                // Recur by reducing both the target sum n and the number of parts k
                for (List<Integer> p : partitionWithKParts(n - i, k - 1, allowed, i)) {
                    List<Integer> newPartition = new ArrayList<>();
                    newPartition.add(i);
                    newPartition.addAll(p);
                    partitions.add(newPartition);
                }
            }
        }

        return partitions;
    }
}
