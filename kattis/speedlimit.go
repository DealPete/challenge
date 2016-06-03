package main

import "fmt"

func main() {
	var pairs, pair1, pair2 int
	var cont bool
	
	fmt.Scan(&pairs)
	cont = pairs != -1
	
	for cont {
		totalh := 0
		totalM := 0
		for i := 0; i < pairs; i++ {
			fmt.Scan(&pair1)
			fmt.Scan(&pair2)
			totalM += pair1*(pair2 - totalh)
			totalh = pair2
		}
		fmt.Println(totalM, " miles\n")
		fmt.Scan(&pairs)
		cont = pairs != -1
	}
}
	