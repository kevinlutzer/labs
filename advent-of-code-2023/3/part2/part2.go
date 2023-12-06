package main

import (
	"fmt"
	"math"
	"os"
	"strings"
	"unicode"
)

func getLines() []string {
	content, err := os.ReadFile("/Users/kevinlutzer/Projects/labs/advent-of-code-2023/3/part2/input.txt")
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

func hasAdjSymbol(x int, y int) [][2]int {
	res := [][2]int{}
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

			v := data[yDiff][xDiff]
			if unicode.IsNumber(v) {
				fmt.Printf("found number %d, at: %+v\n", v-48, [2]int{xDiff, yDiff})
				res = append(res, [2]int{xDiff, yDiff})
			}
		}
	}

	return res
}

func getNumberAtCoor(x int, y int) (int, int, int) {
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

	pos := start
	for pos < (len(data[y])) {
		_rune = data[y][pos]
		if unicode.IsNumber(_rune) {
			digits = append(digits, int(_rune-48))
		} else {
			break
		}

		pos += 1
	}

	val := 0
	for i, digit := range digits {
		val += digit * int(math.Pow(10, (float64(len(digits)-i-1))))
	}

	return val, len(digits), start
}

func main() {

	m := make(map[string]map[string]int)

	sum := 0
	for y, row := range data {
		for x, _rune := range row {
			if _rune == '*' {
				// star map
				starKey := fmt.Sprintf("%d,%d", x, y)
				starMap, ok := m[starKey]
				if !ok {
					starMap = make(map[string]int)
				}

				numCoor := hasAdjSymbol(x, y)

				for _, coor := range numCoor {
					xDiff := coor[0]
					yDiff := coor[1]
					val, _, start := getNumberAtCoor(xDiff, yDiff)
					valuekey := fmt.Sprintf("%d,%d", start, yDiff)
					if _, ok := starMap[valuekey]; !ok {
						fmt.Printf("adding %d at: %+v\n", val, valuekey)
						starMap[valuekey] = val
					}
				}

				fmt.Println("")
				m[starKey] = starMap
			}

		}
	}

	for startKey, val := range m {
		if len(val) > 1 {
			fmt.Printf("star at: %+v\n", startKey)
			starSum := 1
			for valKey, val := range val {
				fmt.Printf("val at: %+v, %d\n", valKey, val)
				starSum *= val
			}
			sum += starSum
			fmt.Println("")
		}
	}

	fmt.Println(sum)
}
