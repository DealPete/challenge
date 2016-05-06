package main

import "fmt"

func main() {
	var N int
	var N2 []bool
	
	fmt.Scan(&N)
	
	for N > 0 {
		N2 = append(N2, N % 2 == 1)
		N /= 2
	}
	
	O := 0
	
	for _, i := range N2 {
		O *= 2
		if i {
			O++
		}
	}
	
	fmt.Print(O)
}