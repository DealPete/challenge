package main

import (
	"fmt"
	"math"
)

func main() {
	var R, C float64
	
	fmt.Scan(&R)
	fmt.Scan(&C)
	
	area := math.Pi * R * R
	innerA := math.Pi * (R - C) * (R - C)
	ratio := innerA/area
	
	fmt.Println(ratio * 100)
}