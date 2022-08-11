package dictionary

import (
	"fmt"
	"os"
	"strings"

	"github.com/saenyakorn/2110413-COMP-SECURITY/enums/method"
	"github.com/saenyakorn/2110413-COMP-SECURITY/internal/password"
)

type Dictionary struct {
	passwords []string
	patterns  [][]string
}

type HashFunction interface {
	Write(p []byte) (n int, err error)
	Sum(b []byte) []byte
}

func NewDictionary(patterns [][]string) (*Dictionary, error) {
	passwords, err := prepareDictionary()
	if err != nil {
		return nil, err
	}

	return &Dictionary{
		passwords,
		patterns,
	}, nil
}

func prepareDictionary() ([]string, error) {
	dat, err := os.ReadFile("internal/dictionary/common-passwords.txt")
	if err != nil {
		return nil, err
	}
	dataStr := string(dat)
	passwords := strings.Split(dataStr, "\n")
	fmt.Println("Loaded", len(passwords), "common passwords")
	fmt.Println("----------------------------------------------------")

	return passwords, nil
}

func (d *Dictionary) FindOriginalPassword(targetHashedPwd string, substitutedPasswords []string) (string, method.Method) {
	// Check with MD5 hash function
	if pwd, correct := password.CheckPasswords(substitutedPasswords, targetHashedPwd, method.MethodMD5); correct {
		return pwd, method.MethodMD5
	}

	// Check with SHA1 Hash function
	if pwd, correct := password.CheckPasswords(substitutedPasswords, targetHashedPwd, method.MethodSHA1); correct {
		return pwd, method.MethodSHA1
	}

	return "", ""
}
