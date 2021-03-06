package string

import (
	"math"
	"strings"
	"unicode"
)

func mostCommonWord(paragraph string, banned []string) string {
	word := []byte{}
	d := make(map[string]int)
	paragraph = strings.ToLower(paragraph)
	for i := 0; i < len(paragraph); i++ {
		if paragraph[i] >= 'a' && paragraph[i] <= 'z' {
			word = append(word, paragraph[i])
		} else {
			if len(word) == 0 {
				continue
			}
			d[string(word)]++
			word = []byte{}
		}
	}
	if len(word) > 0 {
		d[string(word)]++
	}

	var res string
	var t int
	t = math.MinInt32
	for k, v := range d {
		pass := false
		for _, word := range banned {
			if word == k {
				pass = true
				break
			}
		}
		if pass {
			continue
		}
		if v >= t {
			t = v
			res = k
		}
	}
	return res
}

func mostCommonWord2(paragraph string, banned []string) string {
	// 使用非字母来分割原句子，strings包值得好好看一下
	words := strings.FieldsFunc(paragraph, func(c rune) bool {
		return !unicode.IsLetter(c)
	})
	mapWords := make(map[string]int)

	for i := 0; i < len(words); i++ {
		word := strings.ToLower(words[i])
		mapWords[word]++
	}

	max := 0
	res := ""
	for word, count := range mapWords {
		if count > max && !inBanned(word, banned) {
			max = count
			res = word
		}
	}

	return res
}

func inBanned(word string, banned []string) bool {
	for _, bannedStr := range banned {
		if word == bannedStr {
			return true
		}
	}

	return false
}
