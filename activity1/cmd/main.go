package main

import (
	"fmt"
	"time"

	bruceforce "github.com/saenyakorn/2110413-COMP-SECURITY/internal/bruce-force"
	"github.com/saenyakorn/2110413-COMP-SECURITY/internal/dictionary"
	"github.com/saenyakorn/2110413-COMP-SECURITY/internal/rainbow"
)

func main() {
	// Prepare all patterns
	var patterns [][]string
	for ch := 'a'; ch <= 'z'; ch++ {
		s := []string{string(ch), string(ch - 'a' + 'A')}
		if ch == 'o' {
			s = append(s, "0")
		}
		if ch == 'l' {
			s = append(s, []string{"i", "I", "1"}...)
		}
		if ch == 'i' {
			continue
		}
		patterns = append(patterns, s)
	}

	// New dictionary
	d, err := dictionary.NewDictionary(patterns)
	if err != nil {
		panic(err)
	}

	// Evaluate GetAllSubstituteText function
	start := time.Now()
	substitutedPasswords := d.GetAllSubstituteText()
	duration := time.Since(start)

	fmt.Println("Substituted Text Size:", len(substitutedPasswords))
	fmt.Println("Get All Substitute Text elapsed time:", duration)
	fmt.Println("Average time per password:", duration/time.Duration(len(substitutedPasswords)))
	fmt.Println("----------------------------------------------------")

	// Find the original password
	{
		answer, method := d.FindOriginalPassword("d54cc1fe76f5186380a0939d2fc1723c44e8a5f7", substitutedPasswords)
		fmt.Println("Answer", answer, "Method", method)
		fmt.Println("----------------------------------------------------")
	}

	// Create Rainbow Table
	{
		start := time.Now()
		table := rainbow.NewRainbowTable(substitutedPasswords)
		duration := time.Since(start)
		fmt.Println("Table Size:", len(table.Table))
		fmt.Println("Create Rainbow Table elapsed time:", duration)
		fmt.Println("Average time per words:", duration/time.Duration(len(table.Table)))
		fmt.Println("----------------------------------------------------")
	}

	// Bruce force attack
	{
		evaluateBruceforce(1)
		evaluateBruceforce(2)
		evaluateBruceforce(3)
		evaluateBruceforce(4)
		evaluateBruceforce(5)
		fmt.Println("----------------------------------------------------")
	}
}

func evaluateBruceforce(length int) {
	bf := bruceforce.NewBruceforce()
	start := time.Now()
	words := bf.GenerateWords(length)
	duration := time.Since(start)
	fmt.Println("Number of words:", len(words))
	fmt.Println("Generate words of length", length, "elapsed time:", duration)
	fmt.Println("Average time per words", duration/time.Duration(len(words)))
}
