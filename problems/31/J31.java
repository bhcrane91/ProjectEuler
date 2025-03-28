import java.util.List;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;
import java.util.Arrays;


class J31 {

	private static final Set<Integer> coins = new HashSet<>(Arrays.asList(200, 100, 50, 20, 10, 5, 2, 1));

	public static void main(String[] args) {
		int n = 200;
        List<List<Integer>> result = partitions(n, null);
        
		/* 
        for (List<Integer> partition : result) {
            System.out.println(partition);
        }
		*/
		
		System.out.println(result.size());
	}

	public static List<List<Integer>> partitions(int n, Integer maxValue) {
        if (maxValue == null) {
            maxValue = n;
        }

        if (n == 0) {
            List<List<Integer>> baseCase = new ArrayList<>();
            baseCase.add(new ArrayList<>());
            return baseCase;
        }
        
        List<List<Integer>> result = new ArrayList<>();
        
        for (int i = Math.min(n, maxValue); i > 0; i--) {
            if (coins.contains(i)) {
                for (List<Integer> partition : partitions(n - i, i)) {
                    List<Integer> newPartition = new ArrayList<>();
                    newPartition.add(i);
                    newPartition.addAll(partition);
                    result.add(newPartition);
                }
            }
        }

        return result;
    }
}
