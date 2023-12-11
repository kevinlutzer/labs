package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func getLines() []string {
	content, err := os.ReadFile("/Users/kevinlutzer/Projects/labs/advent-of-code-2023/4/part1/input.txt")
	if err != nil {
		panic(err.Error())
	}

	lines := strings.Split(string(content[:]), "\n")

	return lines[:len(lines)-1]
}

func getWinningNumbers(line string) []int {
	colonI := strings.Index(line, ":")
	breakI := strings.Index(line, "|")

	numStr := line[colonI+1 : breakI]
	trimmed := strings.TrimSpace(numStr)
	strNums := strings.Split(trimmed, " ")

	nums := []int{}
	for _, str := range strNums {
		trimmedNums := strings.TrimSpace(str)
		if trimmedNums == "" {
			continue
		}

		val, err := strconv.Atoi(trimmedNums)
		if err != nil {
			panic(err.Error())
		}
		nums = append(nums, val)
	}

	return nums
}

func getMyNumbers(line string) []int {
	breakI := strings.Index(line, "|")

	numStr := line[breakI+1:]
	trimmed := strings.TrimSpace(numStr)
	strNums := strings.Split(trimmed, " ")

	nums := []int{}
	for _, str := range strNums {
		trimmedNums := strings.TrimSpace(str)
		if trimmedNums == "" {
			continue
		}

		val, err := strconv.Atoi(trimmedNums)
		if err != nil {
			panic(err.Error())
		}
		nums = append(nums, val)
	}

	return nums
}

func main() {
	sum := 0
	lines := getLines()
	for _, line := range lines {
		win := getWinningNumbers(line)
		mine := getMyNumbers(line)
		// fmt.Printf("winning: %+v, mine: %+v, line: %+s\n", win, mine, line)

		mineMap := make(map[int]interface{})
		for _, num := range mine {
			mineMap[num] = nil
		}

		val := 0
		matches := 0
		for _, num := range win {
			if _, ok := mineMap[num]; ok {
				if matches == 0 {
					val = 1
				} else {
					val *= 2
				}
				matches += 1
			}
		}

		fmt.Printf("line: %+v matches: %d, val: %d\n", line, matches, val)

		sum += val
	}

	fmt.Printf("sum: %d\n", sum)
}
