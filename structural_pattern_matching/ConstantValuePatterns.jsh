enum Color {
    RED, GREEN, BLUE;
}

public class Main {
    static void processColor(Color color) {
        switch (color) {
            case RED -> System.out.println("It's red!");
            case GREEN -> System.out.println("It's green!");
            case BLUE -> System.out.println("It's blue!");
            default -> System.out.println("Unknown color");
        }
    }

    public static void main(String[] args) {
        processColor(Color.RED);   // Output: It's red!
        processColor(Color.GREEN); // Output: It's green!
    }
}