package password

import (
	"github.com/saenyakorn/2110413-COMP-SECURITY/enums/method"
	"github.com/saenyakorn/2110413-COMP-SECURITY/internal/hasher"
)

func CheckPasswords(passwords []string, targetHahsedPwd string, m method.Method) (string, bool) {
	for _, pwd := range passwords {

		var hashedPwd string
		switch m {
		case method.MethodMD5:
			hashedPwd = hasher.GetMD5Hash(pwd)
		case method.MethodSHA1:
			hashedPwd = hasher.GetSHA1Hash(pwd)
		}

		if hashedPwd == targetHahsedPwd {
			return pwd, true
		}
	}

	return "", false
}
