package main

import (
	"fmt"
	"strconv"
)

func main() {
	var n, p int
	
	fmt.Scan(&n)
	
	total := 0
	for i := 0; i < n; i++ {
		fmt.Scan(&p)
		str := strconv.Itoa(p)
		base, _ := strconv.Atoi(str[:len(str) - 1])
		exp, _ := strconv.Atoi(str[len(str) - 1:])
		
		powTotal := 1
		for j:=0;j < exp;j++ {
			powTotal *= base
		}
		
		total += powTotal
	}
	
	fmt.Print(total)
}