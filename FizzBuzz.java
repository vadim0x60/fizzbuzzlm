public class FizzBuzz {
    public static String fizzBuzz(int num) {
        String fb = (num % 3 == 0 ? "Fizz" : "") + (num % 5 == 0 ? "Buzz" : "");
        if (fb.isEmpty()) return String.valueOf(num);
        else return fb;
    }

    public static void main(String[] args) {
        for (int number = 1; number <= 100; number++) {
            System.out.println(fizzBuzz(number));
        }
    }
}