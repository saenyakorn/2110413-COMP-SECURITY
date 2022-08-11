package dictionary

import "sync"

type Queue struct {
	item  string
	start int
}

func remove(slice []string, s int) []string {
	sliceCopy := make([]string, len(slice))
	copy(sliceCopy, slice)
	return append(sliceCopy[:s], sliceCopy[s+1:]...)
}

func (d *Dictionary) SubstituteText(text string) []string {
	results := make([]string, 0)
	queue := []Queue{
		{text, 0},
	}

	for len(queue) > 0 {
		target := queue[0]
		results = append(results, target.item)
		queue = queue[1:]
		for i := target.start; i < len(target.item); i++ {
			for _, p := range d.patterns {
				for pIdx, s := range p {
					// Ignore the unmatch pattern
					if s != string(target.item[i]) {
						continue
					}
					// Change it to many form and then add them to queue
					removedP := remove(p, pIdx)
					for _, s := range removedP {
						newText := target.item[:i] + s + target.item[i+1:]
						queue = append(queue, Queue{newText, i + 1})
					}
				}
			}
		}
	}

	return results
}

func (d *Dictionary) GetAllSubstituteText() []string {
	var (
		wg      sync.WaitGroup
		mutex   sync.Mutex
		results = make([]string, 0)
	)

	for _, pwd := range d.passwords {
		wg.Add(1)
		go func(pwd string) {
			defer wg.Done()

			pwds := d.SubstituteText(pwd)
			mutex.Lock()
			results = append(results, pwds...)
			mutex.Unlock()
		}(pwd)
	}
	wg.Wait()

	return results
}
