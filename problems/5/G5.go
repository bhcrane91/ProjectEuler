package main 

import (
	"fmt"
)

func gcd(a int, b int) int {
	for b != 0 {
		temp := b 
		b = a % b 
		a = temp
	}
	return a
}

func lcm(a int, b int) int {
	return (a * b) / gcd(a,b)
}

func main() {
	ans := 1 
	n := 20
	for i := 1; i < n; i++ {
		ans = lcm(i,ans)
	}
	fmt.Printf("LCM of numbers 1 to %d: %d\n",n,ans)
}