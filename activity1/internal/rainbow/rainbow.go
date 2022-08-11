package rainbow

import (
	"github.com/saenyakorn/2110413-COMP-SECURITY/internal/hasher"
)

type RainbowTable struct {
	Table map[string]string
}

func NewRainbowTable(words []string) *RainbowTable {
	return &RainbowTable{
		Table: createTable(words),
	}
}

func createTable(words []string) map[string]string {
	table := make(map[string]string)

	for _, item := range words {
		hashedItem := hasher.GetSHA1Hash(item)
		table[item] = hashedItem
	}

	return table
}
