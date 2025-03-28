import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class J42 {
	public static void main(String[] args) {
		String filePath = "words.txt"; // Replace with your file path
        List<String> names = new ArrayList<>();

        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = br.readLine()) != null) {
                // Remove quotes and split by comma
                String[] splitNames = line.replace("\"", "").split(",");
                Collections.addAll(names, splitNames);
            }
        } catch (IOException e) {
            System.err.println("Error reading the file: " + e.getMessage());
        }

		Set<Integer> triangles = new HashSet<>();
		for (int i = 0; i < 30; i++) {
			triangles.add(i * (i+1) / 2);
		}

		int sum = 0;
		for (String name: names) {
			int nSum = 0;
			for (char letter: name.toCharArray()) {
				nSum += ((int) letter) - 64;
			}
			sum += triangles.contains(nSum) ? 1 : 0;
		}
		System.out.println(sum);
	}
}
