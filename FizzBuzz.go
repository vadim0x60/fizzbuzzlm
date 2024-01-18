package main

import (
	"fmt" 
	"strconv"
)

func fizzbuzz(num int) string {
	fb := ""
	
	if num % 3 == 0 {
		fb += "Fizz"
	}
	if num % 5 == 0 {
		fb += "Buzz"
	}
	if fb == "" {
		fb = strconv.Itoa(num)
	}

	return fb
}

func main() {
	for i := 1; i <= 100; i++ {
		fmt.Println(fizzbuzz(i))
	}
}