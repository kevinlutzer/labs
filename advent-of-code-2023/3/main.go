package main

import (
	"fmt"
	"math"
	"os"
	"strings"
	"unicode"
)

func getLines() []string {
	content, err := os.ReadFile("/Users/kevinlutzer/Projects/labs/advent-of-code-2023/3/input.txt")
	if err != nil {
		panic(err.Error())
	}

	lines := strings.Split(string(content[:]), "\n")

	return lines[:len(lines)-1]
}

var data = [][]rune{}

func init() {
	lines := getLines()
	data = make([][]rune, len(lines))
	for i, line := range lines {
		data[i] = make([]rune, len(line))
		for j, _rune := range line {
			data[i][j] = _rune
		}
	}
}

func hasAdjSymbol(x int, y int) bool {
	coor := []int{-1, 0, 1}
	for _, yCoor := range coor {
		for _, xCoor := range coor {
			// Don't look at the actuall rune we are checking
			if xCoor == 0 && yCoor == 0 {
				continue
			}

			yDiff := y + yCoor
			xDiff := x + xCoor

			// Check that symbol is in range
			if !(yDiff >= 0 && yDiff < len(data) && xDiff >= 0 && xDiff < len(data[yDiff])) {
				continue
			}

			if isSymbol(xDiff, yDiff) {
				return true
			}
		}
	}

	return false
}

func isSymbol(x int, y int) bool {
	_rune := data[y][x]
	return !unicode.IsNumber(_rune) && _rune != '.'
}

func getNumberAtCoor(x int, y int) (int, int) {
	var _rune rune
	digits := []int{}

	start := x
	for start-1 >= 0 {
		if unicode.IsNumber(data[y][start-1]) {
			start -= 1
			continue
		}

		break
	}

	for start < (len(data[y])) {
		_rune = data[y][start]
		if unicode.IsNumber(_rune) {
			digits = append(digits, int(_rune-48))
		} else {
			break
		}

		start += 1
	}

	val := 0
	for i, digit := range digits {
		val += digit * int(math.Pow(10, (float64(len(digits)-i-1))))
	}

	return val, len(digits)
}

func main() {

	// m := make(map[string]int)

	sum := 0
	for y, row := range data {
		for x, _rune := range row {
			offset := 0

			if unicode.IsNumber(_rune) {
				if h := hasAdjSymbol(x+offset, y); h {
					fmt.Println("Found symbol at", x+offset, y)
					val, l := getNumberAtCoor(x+offset, y)
					offset += l
					fmt.Printf("Value, new x: %d, %+v\n", x, val)
					fmt.Println()
					// m[fmt.Sprintf("%d,%d", x-start, y)] = val
				}
			}

		}
	}

	fmt.Println(sum)
}
