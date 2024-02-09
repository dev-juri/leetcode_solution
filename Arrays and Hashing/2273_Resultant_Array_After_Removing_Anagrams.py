class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        seen = {}
        start = 0

        while start < len(words):
            sorted_word = "".join(sorted(words[start]))
            if start == 0:
                seen[start] = sorted_word
                start += 1
                continue

            if ((start - 1) in seen) and (seen[start - 1] == sorted_word):
                words.remove(words[start])
                continue

            seen[start] = sorted_word
            start += 1

        return words
