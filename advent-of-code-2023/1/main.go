package main

import (
	"fmt"
	"os"
	"strings"
	"unicode"
)

var wToI = make(map[string]int)

func init() {
	wToI["zero"] = 0
	wToI["one"] = 1
	wToI["two"] = 2
	wToI["three"] = 3
	wToI["four"] = 4
	wToI["five"] = 5
	wToI["six"] = 6
	wToI["seven"] = 7
	wToI["eight"] = 8
	wToI["nine"] = 9
}

func getNumberFromStr(s string) int {
	for k, v := range wToI {
		i := strings.Index(s, k)
		if i == 0 {
			return v
		}
	}

	return -1
}

func main() {
	content, err := os.ReadFile("/Users/kevinlutzer/Projects/labs/advent-of-code-2023/1/input.txt")
	if err != nil {
		panic(err.Error())
	}

	lines := strings.Split(string(content[:]), "\n")

	var first *int
	var last int

	sum := 0

	for i, line := range lines {

		first = nil
		if i == len(lines)-1 {
			continue
		}

		for j, c := range line {

			if unicode.IsNumber(c) {
				if first == nil {
					first = new(int)
					*first = int(c - 48) // 0 starts at 48
				}

				last = int(c - 48)
			} else if n := getNumberFromStr(line[j:]); n > -1 {
				if first == nil {
					first = new(int)
					*first = n
				}
				last = n
			}

			// fmt.Printf("%c, %+v, %d\n", c, unicode.IsNumber(c), getNumberFromStr(line[j:]))
		}

		fmt.Printf("GOOD %d, %d, %d, %s\n", i, *first, last, line)

		sum += 10**first + last

	}

	fmt.Printf("%d \n", sum)

}
