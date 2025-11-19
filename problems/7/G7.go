package main 

import (
	"fmt"
	"math"
)

func check_prime(n int) int {
	if n <= 1 { return 0 }
	if n == 2 { return 1 }
	if n % 2 == 0 { return 0 }
	for i := 3; i < int(math.Sqrt(float64(n)))+1; i+=2 {
		if n % i == 0 { return 0 }
	}
	return 1
}

func main() {
	prime := 3
	n := 1
	for n < 10001 {
		n += check_prime(prime)
		prime += 2
	}
	fmt.Printf("%dst prime = %d\n",n,prime - 2)
}