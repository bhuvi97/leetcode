class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = {}
        for word in strs:
            sign = self.get_signature(word)
            if sign in anagrams:
                anagrams[sign].append(word)
            else:
                anagrams[sign] = [word]

        return [values for key, values in anagrams.items()]

    def get_signature(self, word) -> tuple:

        count = [0]*26

        for letter in word:
            count[ord(letter) - ord("a")] += 1

        return tuple(count)