# your code goes here!

class Anagram:

    def __init__(self, word):
        self.word = word.lower()

    def match(self, words):
        matched_anagrams = []
        normalized_word = sorted(self.word)

        for candidate in words:
            if isinstance(candidate, str) and self.word != candidate.lower():
                if sorted(candidate.lower()) == normalized_word:
                    matched_anagrams.append(candidate)

        return matched_anagrams
    