package main 

import (
	"fmt"
)

func collatz(n int) (int, int) {
	i := 1
	x := n
	for x != 1 {
		if x % 2 == 0 {
			x /= 2
		} else {
			x = 3*x + 1
		}
		i += 1
	}
	return i,n 
}
func main() {
	max := 0
	num := 0
	t := 1000000
	for i := 1; i < t; i++ {
		curr, cn := collatz(i)
		if curr > max {
			max = curr
			num = cn
		}
	}
	fmt.Printf("Maximum Collatz Sequence for c[0] < %d: c[0] = %d | Length: %d\n",t,num,max)
}