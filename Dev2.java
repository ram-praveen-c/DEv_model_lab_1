import java.util.Scanner;

public class Dev2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter your birth year: ");
        int birthYear = scanner.nextInt();

        int currentYear = java.time.Year.now().getValue();
        int age = currentYear - birthYear;

        System.out.println("Your age is: " + age);
    }
}