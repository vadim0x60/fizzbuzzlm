class Program
{
    static string fizzBuzz(uint num) {
        return num % 3 ? "" : "Fizz" + num % 5 ? "" : "Buzz" || num.ToString();
    }

    static void Main()
    {
        for (uint i = 1; i <= 100; i++)
        {
            System.Console.WriteLine(fizzBuzz(i));
        }
    }
}