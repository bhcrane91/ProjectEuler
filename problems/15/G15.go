package main

import (
	"fmt"
)

func main() {
	n := 20 
	triangle := make([]int, n*2)
	triangle[0] = 1
	max := 0
	for row := 0; row < 2*n; row++ {
		for i := 0; i < 2*n; i++ {
			triangle[i] += triangle[(i+1)%(2*n)]
			if triangle[i] > max {
				max = triangle[i]
			}
		}
	}
	fmt.Printf("Paths in %dx%d square: %d\n",n,n,max)
}