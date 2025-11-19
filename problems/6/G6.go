package main 

import (
	"fmt"
)

func main() {
	n := 100
	sum_squares := (n * (n+1) * (2*n + 1)) / 6
	square_sums := ((n * (n+1)) / 2)
	square_sums *= square_sums 
	fmt.Printf("%d\n",square_sums - sum_squares)
}