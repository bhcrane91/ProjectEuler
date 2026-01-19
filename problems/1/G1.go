package main

import "fmt"

func main() {

	ans := 0

	for i := 1; i < 1000; i++ {
		if i%3 == 0 || i%5 == 0 {
			ans += i
		}
	}

	fmt.Println("Sum of multiples of 3 or 5 below 1000:",ans)

}