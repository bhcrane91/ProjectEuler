import java.util.Arrays;

class J41 {
	public static void main(String[] args) {
		String pan = "987654321";

		generatePermutations(pan.toCharArray());
	}

	public static boolean checkPrime(int n) {
		if (n < 2) return false;
		if (n == 2) return true;
		if (n % 2 == 0) return false;
		for (int i = 3; i < (int)Math.sqrt(n)+1; i+=2) {
			if (n % i == 0) return false;
		}
		return true;
	}

	public static void generatePermutations(char[] arr) {
        Arrays.sort(arr); // Start with the smallest permutation
        do {
			char rra = arr;
			reverse(rra)
            System.out.println(reverse(Arrays.toString(arr),0,arr.length));
        } while (nextPermutation(arr));
    }

    private static boolean nextPermutation(char[] arr) {
        int i = arr.length - 2;
        while (i >= 0 && arr[i] >= arr[i + 1]) {
            i--;
        }
        if (i < 0) {
            return false; // No more permutations
        }
        int j = arr.length - 1;
        while (arr[j] <= arr[i]) {
            j--;
        }
        swap(arr, i, j);
        reverse(arr, i + 1, arr.length - 1);
        return true;
    }

    private static void swap(char[] arr, int i, int j) {
        char temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    private static void reverse(char[] arr, int start, int end) {
        while (start < end) {
            swap(arr, start, end);
            start++;
            end--;
        }
    }


}
