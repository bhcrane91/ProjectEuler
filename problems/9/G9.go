package main 

import (
	"fmt"
)

func main() {
	for a := 1; a < 1000; a++ {
		for b := a; b < (1000-a); b++ {
			c := 1000 - b - a
			if a*a + b*b == c*c {
				fmt.Printf("Triple: (%d,%d,%d) | Product: %d\n",a,b,c,a*b*c)
				break
			}
		}
	}
}