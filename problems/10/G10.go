package main 

import (
	"fmt"
	"math"
)

func check_prime(n int) bool {
	if n <= 1 { return false }
	if n == 2 { return true }
	if n % 2 == 0 { return false }
	for i := 3; i < int(math.Sqrt(float64(n)))+1; i+=2 {
		if n % i == 0 { return false }
	}
	return true
}

func main() {
	limit := 2000000
	ans := 2 
	numP := 1
	for i := 1; i < limit; i += 2 {
		if check_prime(i) {
			ans += i 
			numP++
		}
	}
	fmt.Printf("Number of Primes below %d: %d | Sum: %d\n",limit,numP,ans)
}