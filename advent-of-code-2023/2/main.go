package main

import (
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

var colorToIndex = make(map[string]int)

func init() {
	colorToIndex["red"] = 0
	colorToIndex["blue"] = 1
	colorToIndex["green"] = 2
}

func getLines() []string {
	content, err := os.ReadFile("/Users/kevinlutzer/Projects/labs/advent-of-code-2023/2/input.txt")
	if err != nil {
		panic(err.Error())
	}

	lines := strings.Split(string(content[:]), "\n")

	return lines[:len(lines)-1]
}

// returns rbg in that order
func getRollValues(str string) [3]int {
	values := [3]int{0, 0, 0}
	rollValues := strings.Split(str, ", ")
	for _, rollValue := range rollValues {
		for k, v := range colorToIndex {
			if strings.Contains(rollValue, k) {
				i, err := strconv.Atoi(strings.Trim(rollValue, " "+k))
				if err != nil {
					panic("Failed to convert : " + strings.Trim(rollValue, " "+k) + " to string")
				}

				values[v] = i
			}
		}
	}
	return values
}

func main() {

	lines := getLines()
	sum := 0

	// var gameNum int
	for _, line := range lines {
		minValues := [3]int{0, 0, 0}

		// gameNum = i + 1
		gameDetailsIndex := strings.Index(line, ":") + 1
		gameDetails := line[gameDetailsIndex:]

		trimmed := strings.TrimSpace(gameDetails)
		rolls := strings.Split(trimmed, ";")

		fmt.Println(line)
		for _, roll := range rolls {
			values := getRollValues(roll)
			// fmt.Printf("roll: %+v, values: %+v\n", roll, values)

			for i := range minValues {
				minValues[i] = int(math.Max(float64(minValues[i]), float64(values[i])))
			}

		}
		// fmt.Printf("%d\n", minValues[0]*minValues[1]*minValues[2])
		sum += minValues[0] * minValues[1] * minValues[2]
	}

	fmt.Printf("\n\n %d \n\n", sum)
}
