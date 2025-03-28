import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;

public class J22 {
    public static void main(String[] args) {
        String filePath = "names.txt"; // Replace with your file path
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

        // Sort the names alphabetically
        Collections.sort(names);

        HashMap<String,Integer> map = new HashMap<>();
        String letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        for (int i = 0; i < letters.length(); i++) {
            map.put(letters.substring(i, i+1), i+1);
        }

        int totalSum = 0; 
        for (int name = 0; name < names.size(); name++) {
            int nameScore = 0;
            String currName = names.get(name);
            for (int letter = 0; letter < currName.length(); letter++) {
                nameScore += map.get(currName.substring(letter, letter+1));
            } 
            nameScore *= (name + 1); 
            totalSum += nameScore; 
        }
        System.out.println(totalSum);
    }
}

