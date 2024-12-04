package main

import (
	"fmt"
	"math"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {

	// filename := "teste.txt"
	filename := "../../data/input.txt"

	data, _ := os.ReadFile(filename)
	lines := strings.Split(strings.TrimSpace(string(data)), "\n")

	var left, right []int
	for _, line := range lines {
		numbers := strings.Fields(line)
		leftNum, _ := strconv.Atoi(numbers[0])
		rightNum, _ := strconv.Atoi(numbers[1])

		left = append(left, leftNum)
		right = append(right, rightNum)
	}

	// Part 1
	sort.Ints(left)
	sort.Ints(right)

	sum := 0
	for i := 0; i < len(left); i++ {
		sum += int(math.Abs(float64(left[i] - right[i])))
	}

	fmt.Println(sum)

	// Part 2
	counter := map[int]int{}

	for _, num := range right {
		counter[num] += 1
	}

	total := 0
	for _, num := range left {
		total += counter[num] * num
	}

	fmt.Println(total)
}
