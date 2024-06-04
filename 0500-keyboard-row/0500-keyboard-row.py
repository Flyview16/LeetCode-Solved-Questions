class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        result = []

        for word in words:
            word_lower = word.lower()
            for row in rows:
                if all(char in row for char in word_lower):
                    result.append(word)
                    break
        return result

        