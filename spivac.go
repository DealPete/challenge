package main

import "fmt"

func main() {
	var hours, minutes int
	
	fmt.Scan(&hours)
	fmt.Scan(&minutes)
	
	minutes -= 45
	if minutes < 0 {
		minutes += 60
		hours--
		if hours < 0 {
			hours = 23
		}
	}
	
	fmt.Println(hours, minutes)
}