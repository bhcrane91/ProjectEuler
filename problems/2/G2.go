package main 

import "fmt" 

func main() {
	
	a := 1
	b := 2
	s := 0
	t := 4000000
	for b < t {
		c := b + a 
		a = b 
		b = c
		if a % 2 == 0 {
			s += a 
		}
	}
	fmt.Printf("Sum of even-valued Fibonacci terms < %d: %d\n",t,s)
}