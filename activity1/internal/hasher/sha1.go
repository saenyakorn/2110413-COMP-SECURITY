package hasher

import (
	"crypto/sha1"
	"encoding/hex"
)

func GetSHA1Hash(data string) string {
	hash := sha1.Sum([]byte(data))
	return hex.EncodeToString(hash[:])
}
