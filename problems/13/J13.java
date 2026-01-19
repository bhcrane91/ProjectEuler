import java.nio.file.Files;
import java.nio.file.Paths;

class J13 {
	public static void main(String[] args) {
		Long sum = 0L;
		try {
    		sum = Files.lines(Paths.get("digits.txt"))
               .mapToLong(line -> Long.parseLong(line.substring(0, 10)))
               .sum();
		} catch (Exception e) {
			System.out.print(e);
			System.exit(0);
		}
		System.out.println(sum);
	}
}
