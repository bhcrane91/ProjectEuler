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
	for i := 1; i < 20; i++ {
		ans = lcm(i,ans)
	}
	fmt.Printf("%d\n",ans)
}