package main

import "fmt"

func main() {
	var cases int
	var nums [20]int
	
	fmt.Scan(&cases)
	
	for i := 0; i < cases; i++ {
		fmt.Scan(&nums[i])
	}
	
	for i := 0; i < cases; i++ {
		if (nums[i] % 2) == 0 {
			fmt.Println(nums[i], "is even")
		} else {
			fmt.Println(nums[i], "is odd")
		}
	}
}