import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;
import java.io.File;

class J11 {
	public static void main(String[] args) {
		List<List<Integer>> nums = new ArrayList<>();
		try(Scanner sc = new Scanner(new File("nums.txt"))) {
			while (sc.hasNextLine()) {
				String[] line = sc.nextLine().split(" ");
				List<Integer> curr = new ArrayList<>();
				for (String s: line) {
					curr.add(Integer.valueOf(s));
				}
				nums.add(curr);
			}
		} catch (Exception e) {
			System.out.println(e);
		}
	}

	public static List<List<Integer>> horizontal(List<List<Integer>> matrix, int subLength) {
		List<List<Integer>> rows = new ArrayList<>();
		for (int i = 0; i < matrix.size(); i++) {
			for (int j = 0; j < (rows.get(i).size() - subLength); j++) {
				rows.add(matrix.get(i).subList(j, j+subLength));
			}
		}
		return rows;
	}

	public static List<List<Integer>> vertical(List<List<Integer>> matrix, int subLength) {
		List<List<Integer>> cols = new ArrayList<>();
		for (int i = 0; i < matrix.get(0).size(); i++) {
			for (int j = 0; j < (matrix.size() - subLength); j++) {
				List<Integer> sub = new ArrayList<>();
				for (int k = j; k < (j + subLength); k++) {
					sub.add(matrix.get(k).get(i));
				}
				cols.add(sub);
			}
		}
		return cols;
	}

	public static List<List<Integer>> diagonalNWSE(List<List<Integer>> matrix, int subLength) {
		List<List<Integer>> diags = new ArrayList<>();
		for (int i = matrix.size()-1; i >= 0; i--) {
		}
	}

	public static List<List<Integer>> diagonalSWNE(List<List<Integer>> matrix, int subLength) {

	}

	public static int[][] listToArr(List<List<Integer>> list) {
		int[][] arr = new int[list.size()][list.get(0).size()];
		for (int i = 0; i < list.size(); i++) {
			for (int j = 0; j < list.get(i).size(); j++) {
				arr[i][j] = list.get(i).get(j);
			}
		}
		return arr;
	}

	public static int[][] horizontal_sub(int[][] arr, int l) {
		int[][] nums = new int[arr.length*(arr[0].length-l+1)][l];
		for (int i = 0; i < arr.length; i++) {
			for (int j = 0; j < arr[i].length-l+1; j++) {
				for (int k = 0; k < l; k++) {
					System.out.println(i+j);
					nums[i+j][k] = arr[i][j+k];
				}
			}
		}
		for (int i = 0; i < nums.length; i++) {
			for (int j = 0; j < nums[i].length; j++) {
				System.out.print(nums[i][j] + " ");
			}
			System.out.println();
		}
		return nums;
	}

	public static int[][] vertical_sub(List<List<Integer>> arr, int l) {
		return null;
	}

	public static int[][] diag_sub_nw_se(List<List<Integer>> arr, int l) {
		return null;
	}

	public static int[][] diag_sub_sw_ne(List<List<Integer>> arr, int l) {
		return null;
	}
}
