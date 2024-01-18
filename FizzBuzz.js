function fizzbuzz(num) {
    return (num % 3 ? "" : "Fizz") + (num % 5 ? "" : "Buzz") || num; 
}

for (let i = 1; i <= 100; i++) {
    console.log(fizzbuzz(i));
}