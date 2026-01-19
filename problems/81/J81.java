import java.io.File;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

class J81 {
	public static void main(String[] args) {
		List<List<Integer>> grid = new ArrayList<>();

		try {
			List<String> lines = Files.readAllLines(Paths.get("matrix.txt"));

        	for (String line : lines) {
            	if (!line.trim().isEmpty()) {
                	List<Integer> row = new ArrayList<>();
                	for (String value : line.split(",")) {
                    	row.add(Integer.parseInt(value.trim()));
                	}
                	grid.add(row);
            	}
        	}
		} catch (Exception e) {
			e.printStackTrace();
			return;
		}

		int max = 0;
        int[][] matrix = new int[grid.size()][];
        for (int i = 0; i < grid.size(); i++) {
            matrix[i] = grid.get(i).stream().mapToInt(Integer::intValue).toArray();
			int newmax = Arrays.stream(matrix[i]).max().getAsInt();
			max = max > newmax ? max : newmax;
        }

		minimumPathSum(toPyramid(matrix, max));
	}

	public static int[][] toPyramid(int[][] matrix, int fill) {
		int side = matrix.length;
		int[][] pyramid = new int[2*side-1][matrix[0].length];
		int p_row = side;

		for (int row = 0; row < side; row++) {
			Arrays.fill(pyramid[row], fill);
			for (int col = 0; col <= row; col++) {
				pyramid[row][col] = matrix[row-col][col];
			}
			
		}

		for (int row = (side-1); row > 0; row--) {
			Arrays.fill(pyramid[p_row], fill);
			for (int col = 0; col < row; col++) {
				pyramid[p_row][col] = matrix[side-col-1][side-row+col];
			}
			p_row++;
		}

		return pyramid;
	}

	public static int minimumPathSum(int[][] pyramid) {
		int[][] top = Arrays.copyOf(pyramid, pyramid[0].length);
		int[][] bot = Arrays.copyOfRange(pyramid, pyramid[0].length-1, pyramid.length);

		for (int row = 1; row < top.length; row++) {
			int[] left = add(roll(top[row-1],1), top[row]);
			int[] right = add(top[row-1],top[row]);
			top[row] = minimum(left, right);
		}

		for (int row = 0; row < bot.length-1; row++) {
			int[] right = add(roll(bot[row], -1), bot[row+1]);
			int[] left = add(bot[row],bot[row+1]);
			bot[row+1] = minimum(left, right);
		}

		System.out.println("Minimum Path Sum = " + bot[bot.length-1][0]);
		return bot[bot.length-1][0];
	}

	public static int mod(int a, int b) {
		return (a % b + b) % b;
	}
	public static int[] add(int[] a, int[] b) {
		if (a.length != b.length) {
			return null;
		}
		int[] sum = new int[a.length];
		for (int i = 0; i < a.length; i++) {
			sum[i] = a[i] + b[i];
		}
		return sum;
	}

	public static int[] roll(int[] arr, int step) {
		if (step == 0) return arr;
		int[] rll = new int[arr.length];
		for (int i = 0; i < arr.length; i++) {
			rll[i] = arr[mod((i-step),arr.length)];
		}
		return rll;
	}

	public static int[] minimum(int[] a, int[] b) {
		int l = a.length > b.length ? a.length : b.length;
		int[] c = new int[l];
		for (int i = 0; i < l; i++) {
			c[i] = a[i] < b[i] ? a[i] : b[i];
		}
		return c;
	}


}
