package main

import (
	"fmt"
	"sort"
	"strconv"
)

func kth_smallest_element(arr []int, start int, end int, k int) int {
	sort.Ints(arr)
	return arr[k-1]
}

func main() {
	arr := []int{1, 2, 10, -1, 3}
	k := 3
	smallest := kth_smallest_element(arr, 0, len(arr), k)
	fmt.Println("Kth Smallest Element: " + strconv.Itoa(smallest))
}
