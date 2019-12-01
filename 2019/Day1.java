import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.stream.Collectors;

public class Day1 {
    public static void main(String[] args) throws IOException {
        System.out.println(
            Files.lines(Paths.get("2019/assets/Day1.modules.txt")).map(Integer::parseInt).map(Day1::calculateFuel).collect(Collectors.summingInt(i -> i))
        );
    }

    private static int calculateFuel(int amount) {
        int current = Math.max((amount/3) - 2, 0);
        if (current > 0) {
            current += calculateFuel(current);
        }
        return current;
    }
}