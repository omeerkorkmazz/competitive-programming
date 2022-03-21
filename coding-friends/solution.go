package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

func minNum(samDaily int32, kellyDaily int32, difference int32) int32 {
	var counter int32
	counter = 1

	samSolved := difference + samDaily
	kellySolved := kellyDaily

	if samSolved == kellySolved && difference == 0 {
		return -1
	}

	for kellySolved <= samSolved {
		counter++
		kellySolved += kellyDaily
		samSolved += samDaily
	}

	return counter
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 16*1024*1024)

	stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
	checkError(err)

	defer stdout.Close()

	writer := bufio.NewWriterSize(stdout, 16*1024*1024)

	samDailyTemp, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
	checkError(err)
	samDaily := int32(samDailyTemp)

	kellyDailyTemp, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
	checkError(err)
	kellyDaily := int32(kellyDailyTemp)

	differenceTemp, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
	checkError(err)
	difference := int32(differenceTemp)

	result := minNum(samDaily, kellyDaily, difference)

	fmt.Fprintf(writer, "%d\n", result)

	writer.Flush()
}

func readLine(reader *bufio.Reader) string {
	str, _, err := reader.ReadLine()
	if err == io.EOF {
		return ""
	}

	return strings.TrimRight(string(str), "\r\n")
}

func checkError(err error) {
	if err != nil {
		panic(err)
	}
}
