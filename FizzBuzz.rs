fn fizzbuzz(num: u32) -> String {
    match (num % 3, num % 5) {
        (0, 0) => String::from("FizzBuzz"),
        (0, _) => String::from("Fizz"),
        (_, 0) => String::from("Buzz"),
        _ => num.to_string(),
    }
}

fn main() {
    for i in 1..=100 {
        println!("{}", fizzbuzz(i));
    }
}