def fizzbuzz(num):
    return "Fizz" * (num % 3 == 0) + "Buzz" * (num % 5 == 0) or str(num)

if __name__ == '__main__':
    for i in range(1, 101):
        print(fizzbuzz(i))