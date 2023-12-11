package main

import (
	"fmt"
	"os"
	"strings"
)

var colorToIndex = make(map[string]int)

func init() {
	colorToIndex["red"] = 0
	colorToIndex["blue"] = 1
	colorToIndex["green"] = 2
}

func getLines() []string {
	content, err := os.ReadFile("/Users/kevinlutzer/Projects/labs/advent-of-code-2023/3/input.txt")
	if err != nil {
		panic(err.Error())
	}

	lines := strings.Split(string(content[:]), "\n")

	return lines[:len(lines)-1]
}

func main() {

	lines := getLines()
	for _, line := range lines {
		fmt.Println(line)
	}
}
