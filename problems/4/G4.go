package main

import (
	"fmt"
	"math"
)

func check_palindrome(s int) bool {
	rev := 0
	temp := s 
	for temp > 0 {
		last := temp % 10
		rev = rev * 10 + last 
		temp /= 10
	}
	return s == rev
}

func main() {
	digits := float64(3) 
	bot := int(math.Pow(10,digits-1))
	top := int(math.Pow(10,digits))
	max := make([]int,3)
	for i := top; i >= bot; i-- {
		for j := i; j >= bot; j-- {
			p := i*j
			if p > max[0] && check_palindrome(p) {
				max[0] = p;
				max[1] = i;
				max[2] = j;
			}
		}
	}
	fmt.Printf("Max: %d | Factors: (%d,%d)\n",max[0],max[1],max[2])
}