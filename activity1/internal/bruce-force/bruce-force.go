package bruceforce

type Bruceforce struct {
}

func NewBruceforce() *Bruceforce {
	return &Bruceforce{}
}

func (b *Bruceforce) GenerateWords(length int) []string {
	stack := make([]string, 0)
	stack = append(stack, "")
	results := make([]string, 0)

	for len(stack) > 0 {
		word := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		if len(word) == length {
			results = append(results, word)
			continue
		}
		for i := 0; i < 26; i++ {
			stack = append(stack, word+string(i+'a'))
			stack = append(stack, word+string(i+'A'))
		}
	}

	return results
}
