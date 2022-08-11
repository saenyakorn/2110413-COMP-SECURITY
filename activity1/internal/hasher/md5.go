package hasher

import (
	"crypto/md5"
	"encoding/hex"
)

func GetMD5Hash(data string) string {
	hash := md5.Sum([]byte(data))
	return hex.EncodeToString(hash[:])
}
