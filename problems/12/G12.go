package main 

import (
	"fmt"
	"math"
)

func main() {
	target := 500
	tri := 1
	itr := 1
	div := 1
	for div < target {
		itr++
		tri += itr
		div = 0 
		for i := 1; i < int(math.Sqrt(float64(tri)))+1; i++ {
			if tri % i == 0 {
				if tri / i == i {
					div++
				} else {
					div += 2
				}
			}
		}
	}
	fmt.Printf("Triangle Number (%d): %d | Divisors: %d\n",itr,tri,div)
}