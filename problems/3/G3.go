package main

import (
	"fmt"
	"math"
)

func prime_factors(n int) []int {
	nums := make([]int, 0)

	for n % 2 == 0 {
		nums = append(nums,n)
		n /= 2
	}

	b := int(math.Sqrt(float64(n)))
	for i := 3; i <= b; i += 2 {
		for n % i == 0 {
			nums = append(nums,i)
			n /= i
		}
	}

	if n > 1 {
		nums = append(nums,n)
	}

	return nums
}

func main() {
	n := 600851475143
	fmt.Printf("Prime Factors of %d: ",n)
	ans := prime_factors(n)
	for _, value := range ans {
          fmt.Printf("%d ", value)
	}
	fmt.Printf("| Largest -> %d\n", ans[len(ans)-1])
}

