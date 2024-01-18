def fizzbuzz(num):
    return ("Fizz" if num % 3 == 0 else "") + ("Buzz" if num % 5 == 0 else "") or str(num)

if __name__ == '__main__':
    for i in range(1, 101):
        print(fizzbuzz(i))